import wx

SPACER = (0, 0)


class SendTab(wx.Panel):
    def __init__(self, parent, wallet):
        super().__init__(parent)
        self.wallet = wallet
        self.create_send_tab()

    def create_send_tab(self):
        receive_text = wx.StaticText(self, label='Receiver Address: ')
        self.receive_address_input = wx.TextCtrl(self)

        amount_text = wx.StaticText(self, label='Iota: ')
        self.amount_input = wx.TextCtrl(self)

        send_button = wx.Button(self, label='Send')

        input_vbox = wx.BoxSizer(wx.VERTICAL)
        input_vbox.Add(receive_text, flag=wx.CENTER)
        input_vbox.Add(self.receive_address_input, flag=wx.EXPAND)
        input_vbox.Add(amount_text, flag=wx.CENTER)
        input_vbox.Add(self.amount_input, flag=wx.CENTER)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(SPACER, proportion=1)
        vbox.Add(input_vbox, proportion=1, flag=(wx.EXPAND | wx.ALL), border=10)
        vbox.Add(send_button, proportion=1, flag=wx.EXPAND)
        vbox.Add(SPACER, proportion=1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(SPACER, proportion=1)
        hbox.Add(vbox, proportion=1, flag=(wx.CENTER | wx.ALL))
        hbox.Add(SPACER, proportion=1)
        self.SetSizer(hbox)

        self.Bind(wx.EVT_BUTTON, self.send_button_clicked, send_button)

    def send_button_clicked(self, event):
        address = self.receive_address_input.GetLineText(0)
        iota_amount = int(self.amount_input.GetLineText(0))

        if iota_amount > self.wallet.balance:
            self.show_insufficient_balance_dialog(iota_amount)
        else:
            self.show_confirm_send_dialog(address, iota_amount)

    def show_confirm_send_dialog(self, address, iota_amount):
        message = (f'You are about to send\n\n' +
                   f'{iota_amount} iota\n\n' +
                   f'to {address}')
        dialog = wx.MessageDialog(
            self,
            message=message,
            caption='Confirm Send',
            style=(wx.YES_NO | wx.NO_DEFAULT),
        )
        response = dialog.ShowModal()
        if response == wx.ID_YES:
            self.wallet.send(address, iota_amount)

    def show_insufficient_balance_dialog(self, iota_amount):
        dialog = wx.MessageDialog(
            self,
            message=f'You do not have enough funds to send {iota_amount} iota',
            caption='Insufficient Balance',
        )
        dialog.ShowModal()


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None, title='SendTab', size=(1000, 600))
    from collections import namedtuple
    wallet = namedtuple('wallet', ['balance'])
    panel = SendTab(frame, wallet(balance=1))
    frame.Show()
    app.MainLoop()