import queue
import traceback
import threading
from typing import Any, Callable, Optional, Tuple

import wx
from iota.adapter import resolve_adapter
from iota.commands.core import GetNodeInfoCommand

from .history import HistoryTab
from .overview import OverviewTab
from .receive import ReceiveTab
from .send import SendTab
from ..wallet import Wallet

QueueType = Tuple[Callable, Tuple, Optional[Callable]]
DEFAULT_URI = 'https://iotanode.us:443'


class WalletWindow(wx.Frame):  # type: ignore
    def __init__(self) -> None:
        super().__init__(
            None,
            title='Iota Wallet',
            size=(1000, 600),
        )

        self.worker = WorkerThread()

        self.panel = wx.Panel(self)
        self.create_status_bar()
        self.add_login_ui()

    def add_login_ui(self) -> None:

        # TODO: Change this to an icon
        text = wx.StaticText(self.panel, label='Iota Wallet')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(text, flag=wx.CENTER)

        self.seed_input = wx.TextCtrl(self.panel)
        self.login_button = wx.Button(self.panel, label='Login')
        login_vbox = wx.BoxSizer(wx.VERTICAL)
        login_vbox.Add(self.seed_input, proportion=1, flag=wx.EXPAND)
        login_vbox.Add(self.login_button, proportion=1, flag=wx.EXPAND)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion=2, flag=(wx.CENTER | wx.ALL), border=20)
        vbox.Add(login_vbox, proportion=1, flag=(wx.EXPAND | wx.ALL), border=20)

        self.panel.SetSizer(vbox)
        self.panel.Layout()

        self.Bind(wx.EVT_BUTTON, self.on_login_clicked, self.login_button)

    def create_status_bar(self) -> None:
        self.status_bar = self.CreateStatusBar()

        # Get the milestone status the first time then set up a timer to
        # periodically check it
        self._update_milestone()

        self._update_milestone_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._update_milestone, self._update_milestone_timer)
        self._update_milestone_timer.Start(15 * 1000)

    def _update_milestone(self,
                          event: Optional[wx.TimerEvent] = None) -> None:
        response = GetNodeInfoCommand(resolve_adapter(DEFAULT_URI))()
        current_milestone = response['latestSolidSubtangleMilestoneIndex']
        latest_milestone = response['latestMilestoneIndex']

        if current_milestone == latest_milestone:
            status = f'Synced: {current_milestone}'
        else:
            status = f'Unsynced: {current_milestone}/{latest_milestone}'

        self.status_bar.PushStatusText(status)

    def on_login_clicked(self,
                         event: wx.CommandEvent) -> None:
        seed = self.seed_input.GetLineText(0)

        # Check seed
        error = ''
        if len(seed) != 81:
            error = 'Error: Seed must be 81 characters'
        else:
            valid_chars = '9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            if not all(char in valid_chars for char in seed):
                error = 'Error: Seed must contain only A-Z or 9'

        if error:
            print(error)
            self.disable_login_button(error)
            wx.CallLater(3 * 1000, self.reenable_login_button)
        else:
            self.wallet = Wallet(
                uri=DEFAULT_URI,
                seed=seed,
            )

            self.worker.send(self.wallet.refresh_account, callback=self.after_account)
            self.disable_login_button('Logging in...')

    def disable_login_button(self,
                             label: str) -> None:
        self.login_button.SetLabel(label)
        self.login_button.Disable()

    def reenable_login_button(self) -> None:
        self.login_button.Enable()
        self.login_button.SetLabel('Login')

    def after_account(self,
                      result: Any) -> None:
        self.transition_to_main_ui()

    def transition_to_main_ui(self) -> None:
        self.panel.DestroyChildren()
        self.create_main_ui()

    def create_main_ui(self) -> None:
        notebook = wx.Notebook(self.panel)

        overview_tab = OverviewTab(notebook, self.wallet)
        send_tab = SendTab(notebook, self.wallet)
        receive_tab = ReceiveTab(notebook, self.wallet)
        history_tab = HistoryTab(notebook, self.wallet)

        notebook.AddPage(overview_tab, 'Overview')
        notebook.AddPage(send_tab, 'Send')
        notebook.AddPage(receive_tab, 'Receive')
        notebook.AddPage(history_tab, 'History')

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(notebook, flag=(wx.EXPAND | wx.ALL), proportion=1)

        self.panel.SetSizer(sizer)
        self.panel.Layout()


class WorkerThread:
    def __init__(self) -> None:
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.queue: queue.Queue[QueueType] = queue.Queue()
        self.thread.start()

    def _run(self) -> None:
        while True:
            command, args, callback = self.queue.get()
            try:
                result = command(*args)
                if callback:
                    wx.CallAfter(callback, result)
            except Exception as e:
                traceback.print_exc()

    def send(self,
             command: Callable,
             args: Tuple = (),
             callback: Optional[Callable] = None) -> None:
        self.queue.put((command, args, callback))


def main() -> None:
    app = wx.App()
    wallet = WalletWindow()
    wallet.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
