import wx


class ReceiveTab(wx.Panel):
    def __init__(self, parent, wallet):
        super().__init__(parent)
        self.wallet = wallet
        self.create_receive_tab()

    def create_receive_tab(self):
        receive_text = wx.StaticText(self, label='Receive Addresses: ')

        self.list_ctrl = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, 'Addresses')
        for address in self.wallet.addresses:
            self.list_ctrl.Append([str(address)])
        self.list_ctrl.SetColumnWidth(0, wx.LIST_AUTOSIZE)

        new_address_button = wx.Button(self, label='Generate New Address')
        self.Bind(wx.EVT_BUTTON, self.new_address_button_clicked, new_address_button)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(receive_text, flag=wx.CENTER)
        vbox.Add(self.list_ctrl, proportion=20, flag=wx.EXPAND)
        vbox.Add(new_address_button, proportion=2, flag=wx.CENTER)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(vbox, proportion=1, flag=(wx.EXPAND | wx.ALL), border=10)

        self.SetSizer(hbox)

    def new_address_button_clicked(self, event):
        new_address = self.wallet.create_new_address()
        self.list_ctrl.Append([new_address])


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, title='ReceiveTab', size=(1000, 600))
    from collections import namedtuple
    wallet = namedtuple('wallet', ['addresses'])
    from iota import Address
    panel = ReceiveTab(frame, wallet(addresses=[Address('ASDF')]))
    frame.Show()
    app.MainLoop()
