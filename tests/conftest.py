import wx

import pytest


@pytest.fixture(scope='function', autouse=True)
def app():
    # wx requires an App object before anything else
    app = wx.App()  # noqa: F841
    yield


@pytest.fixture(scope='function')
def frame():
    yield wx.Frame(None, title='Test', size=(1000, 600))
