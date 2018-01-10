import wx

SPACER = (0, 0)


class SendTab(wx.Panel):
    def __init__(self, parent, wallet):
        super().__init__(parent)
        self.create_send_tab()

    def create_send_tab(self):
        receive_text = wx.StaticText(self, label='Receiver Address: ')
        receive_address_input = wx.TextCtrl(self)

        amount_text = wx.StaticText(self, label='Iota: ')
        amount_input = wx.TextCtrl(self)

        send_button = wx.Button(self, label='Send')

        input_vbox = wx.BoxSizer(wx.VERTICAL)
        input_vbox.Add(receive_text, flag=wx.CENTER)
        input_vbox.Add(receive_address_input, flag=wx.EXPAND)
        input_vbox.Add(amount_text, flag=wx.CENTER)
        input_vbox.Add(amount_input, flag=wx.CENTER)

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
