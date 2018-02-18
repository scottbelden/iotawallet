import os
import shutil
import wx

import pytest

# Make a directory to store screenshots in the case of a failure
SCREENSHOT_DIR = os.path.join('tests', '_failure_screenshots')
if os.path.exists(SCREENSHOT_DIR):
    shutil.rmtree(SCREENSHOT_DIR)
os.makedirs(SCREENSHOT_DIR)


@pytest.fixture(scope='function', autouse=True)
def app():
    # wx requires an App object before anything else
    yield wx.App()


@pytest.fixture(scope='function')
def frame():
    yield wx.Frame(None, title='Test', size=(1000, 600))


def pytest_exception_interact(node, call, report):
    frame = node.funcargs['frame']
    app = node.funcargs['app']
    function_name = node.name

    def take_screenshot():
        rect = frame.GetRect()
        bmp = wx.Bitmap(rect.width, rect.height)
        memory = wx.MemoryDC()
        memory.SelectObject(bmp)
        memory.Blit(0,
                    0,
                    rect.width,
                    rect.height,
                    wx.ScreenDC(),
                    rect.x,
                    rect.y)
        memory.SelectObject(wx.NullBitmap)
        filename = os.path.join(SCREENSHOT_DIR, function_name + '.png')
        bmp.ConvertToImage().SaveFile(filename, wx.BITMAP_TYPE_PNG)

    wx.CallLater(.25 * 1000, take_screenshot)
    wx.CallLater(.5 * 1000, app.ExitMainLoop)

    frame.Show()
    app.MainLoop()
