from unittest.mock import MagicMock

from iota import Address

from iotawallet.gui.receive import ReceiveTab, DEFAULT_COLUMN_WIDTH


def test_panel_creation(frame):
    mock_wallet = MagicMock()

    ReceiveTab(frame, mock_wallet)


def test_receive_column_width_with_address(frame):
    mock_wallet = MagicMock(addresses=[Address('ASDF')])

    panel = ReceiveTab(frame, mock_wallet)
    assert panel.list_ctrl.GetColumnWidth(0) >= DEFAULT_COLUMN_WIDTH


def test_receive_column_width_without_address(frame):
    mock_wallet = MagicMock(addresses=[])

    panel = ReceiveTab(frame, mock_wallet)
    assert panel.list_ctrl.GetColumnWidth(0) >= DEFAULT_COLUMN_WIDTH
