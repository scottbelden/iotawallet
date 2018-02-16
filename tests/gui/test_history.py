from unittest.mock import MagicMock

from iotawallet.gui.history import HistoryTab


def test_panel_creation(frame):
    mock_wallet = MagicMock()

    HistoryTab(frame, mock_wallet)
