from unittest.mock import MagicMock

from iotawallet.gui.send import SendTab


def test_panel_creation(frame):
    mock_wallet = MagicMock()

    SendTab(frame, mock_wallet)
