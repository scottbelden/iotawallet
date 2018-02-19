from unittest.mock import MagicMock, patch
import wx
import pytest

from iota import BundleHash

from iotawallet.gui.defaults import DEFAULT_COLUMN_WIDTH
from iotawallet.gui.history import HistoryTab


@pytest.fixture(scope='function')
def populated_panel(frame):
    bundles = {
        'confirmed': [MagicMock(hash=BundleHash('A'))],
        'unconfirmed': [MagicMock(hash=BundleHash('B'))],
    }
    mock_wallet = MagicMock(bundles=bundles)

    yield HistoryTab(frame, mock_wallet)


def test_panel_creation(frame):
    mock_wallet = MagicMock()
    HistoryTab(frame, mock_wallet)


def test_history_column_width_with_transactions(populated_panel):
    assert populated_panel.transactions.GetColumnWidth(0) > DEFAULT_COLUMN_WIDTH


def test_history_column_width_without_transactions(frame):
    mock_wallet = MagicMock()
    panel = HistoryTab(frame, mock_wallet)
    assert panel.transactions.GetColumnWidth(0) == DEFAULT_COLUMN_WIDTH


def test_right_click_transaction(populated_panel):
    event = wx.ListEvent(wx.wxEVT_LIST_ITEM_RIGHT_CLICK, populated_panel.transactions.GetId())
    event.SetItem(populated_panel.transactions.GetItem(0))

    # Patch PopupMenu so that the menu isn't actually created since there
    # doesn't seem to be a good way to cause it to go away
    with patch.object(populated_panel, 'PopupMenu', (lambda _: None)):
        populated_panel.GetEventHandler().ProcessEvent(event)

    event = wx.CommandEvent(wx.wxEVT_MENU, id=populated_panel.popup_menu.FindItemByPosition(0).GetId())
    populated_panel.GetEventHandler().ProcessEvent(event)
