from unittest.mock import MagicMock

from iotawallet.gui.overview import OverviewTab


def test_panel_creation(frame):
    mock_wallet = MagicMock()

    OverviewTab(frame, mock_wallet)
