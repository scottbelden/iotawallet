from unittest.mock import MagicMock

from iota import BundleHash

from iotawallet.gui.defaults import DEFAULT_COLUMN_WIDTH
from iotawallet.gui.history import HistoryTab


def test_panel_creation(frame):
    mock_wallet = MagicMock()

    HistoryTab(frame, mock_wallet)


def test_history_column_width_with_transactions(frame):
    bundles = {
        'confirmed': [MagicMock(hash=BundleHash('A'))],
        'unconfirmed': [MagicMock(hash=BundleHash('B'))],
    }
    mock_wallet = MagicMock(bundles=bundles)

    panel = HistoryTab(frame, mock_wallet)
    assert panel.transactions.GetColumnWidth(0) > DEFAULT_COLUMN_WIDTH


def test_history_column_width_without_transactions(frame):
    mock_wallet = MagicMock()

    panel = HistoryTab(frame, mock_wallet)
    assert panel.transactions.GetColumnWidth(0) == DEFAULT_COLUMN_WIDTH
