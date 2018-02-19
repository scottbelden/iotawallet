from unittest.mock import MagicMock, patch
import pytest
import wx

from iota import Address

from iotawallet.gui.defaults import DEFAULT_COLUMN_WIDTH
from iotawallet.gui.receive import ReceiveTab


@pytest.fixture(scope='function')
def populated_panel(frame):
    mock_wallet = MagicMock(addresses=[Address('ASDF')])
    yield ReceiveTab(frame, mock_wallet)


def test_panel_creation(frame):
    mock_wallet = MagicMock()
    ReceiveTab(frame, mock_wallet)


def test_receive_column_width_with_address(populated_panel):
    assert populated_panel.list_ctrl.GetColumnWidth(0) > DEFAULT_COLUMN_WIDTH


def test_receive_column_width_without_address(frame):
    mock_wallet = MagicMock(addresses=[])
    panel = ReceiveTab(frame, mock_wallet)
    assert panel.list_ctrl.GetColumnWidth(0) == DEFAULT_COLUMN_WIDTH


def test_right_click_address(populated_panel):
    event = wx.ListEvent(wx.wxEVT_LIST_ITEM_RIGHT_CLICK, populated_panel.list_ctrl.GetId())
    event.SetItem(populated_panel.list_ctrl.GetItem(0))

    # Patch PopupMenu so that the menu isn't actually created since there
    # doesn't seem to be a good way to cause it to go away
    with patch.object(populated_panel, 'PopupMenu', (lambda _: None)):
        populated_panel.GetEventHandler().ProcessEvent(event)

    event = wx.CommandEvent(wx.wxEVT_MENU, id=populated_panel.popup_menu.FindItemByPosition(0).GetId())
    populated_panel.GetEventHandler().ProcessEvent(event)
