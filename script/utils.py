import time
import baiduApi
from win32com.client import Dispatch
op = Dispatch("op.opsoft")


def writeText(text):
    if text == 'ch.1993.com':
        writeText('ch')
        op.KeyPress('190')
        writeText('1993')
        op.KeyPress('190')
        writeText('com')
    else:
        for key in text:
            time.sleep(0.25)
            if key.isupper():
                op.KeyDown(16)
                time.sleep(0.1)
                op.KeyPressChar(key)
                op.KeyUp(16)
            else:
                op.KeyPressChar(key)


def pressKeyGroup(key1, key2):
    op.KeyDown(key1)
    time.sleep(0.1)
    op.KeyPress(key2)
    op.KeyUp(key1)


def getGameVerificationCode():
    try:
        hwnd = op.findWindow('', '乾坤辅助平台')
        ret = op.bindWindow(hwnd, "normal", "normal", "normal", 0)
        print(ret)
        op_ret = op.Capture(120, 250, 330, 283, "screen.bmp")
        s = op.ocr(120, 250, 330, 283, "000000-993d27|000000-000000", 0.9)
        baiduRetStr = baiduApi.getImageText('screen.bmp')
        print(baiduRetStr['words_result'])
        verificationCode = ''
        for item in baiduRetStr['words_result']:
            verificationCode = verificationCode + item['words']
        print(verificationCode)
        return verificationCode
    except IOError:
        print(0)


if __name__ == "__main__":
    time.sleep(3)
    writeText('ch.1993.com')
