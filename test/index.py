from win32com.client import Dispatch
import baiduApi
import json
# create op instance 创建op对象
op=Dispatch("op.opsoft")
# print version of op 打印op插件的版本
print(op.Ver())

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

