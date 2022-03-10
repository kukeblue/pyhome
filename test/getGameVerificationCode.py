from win32com.client import Dispatch
import baiduApi

op = Dispatch("op.opsoft")
print(op.Ver())


def getGameVerificationCode():
    try:
        hwnd = op.findWindow('', '乾坤辅助平台')
        ret = op.bindWindow(hwnd, "normal", "normal", "normal", 0)
        print(ret)
        op.Capture(140, 180, 350, 223, "screen.bmp")
        baiduRetStr = baiduApi.getImageText('screen.bmp')
        print(baiduRetStr['words_result'])
        verificationCode = ''
        for item in baiduRetStr['words_result']:
            verificationCode = verificationCode + item['words']
        print(verificationCode)
        return verificationCode
    except IOError:
        print(0)
        return 0

