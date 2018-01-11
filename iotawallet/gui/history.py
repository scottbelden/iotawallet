import wx

from ..wallet import Wallet


class HistoryTab(wx.Panel):  # type: ignore
    def __init__(self,
                 parent: wx.Window,
                 wallet: Wallet) -> None:
        super().__init__(parent)
        self.wallet = wallet
        self.create_history_tab()

    def create_history_tab(self) -> None:
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, label='History')
        hbox.Add(text, flag=wx.ALL)
        self.SetSizer(hbox)


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, title='HistoryTab', size=(1000, 600))
    panel = HistoryTab(frame, None)  # type: ignore
    frame.Show()
    app.MainLoop()
