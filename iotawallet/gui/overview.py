import wx


class OverviewTab(wx.Panel):
    def __init__(self, parent, wallet):
        super().__init__(parent)
        self.wallet = wallet
        self.create_overview_tab()

    def create_overview_tab(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        balance_text = wx.StaticText(self, label=f'Balance: {self.wallet.balance}')
        hbox.Add(balance_text, flag=wx.ALL)
        self.SetSizer(hbox)


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, title='OverviewTab', size=(1000, 600))
    from collections import namedtuple
    wallet = namedtuple('wallet', ['balance'])
    panel = OverviewTab(frame, wallet(balance=1))
    frame.Show()
    app.MainLoop()
