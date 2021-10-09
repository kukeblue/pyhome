from ctypes import windll, byref, c_ubyte
from ctypes.wintypes import RECT, HWND
import numpy as np

# GetDC = windll.user32.GetDC
# CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
# GetClientRect = windll.user32.GetClientRect
# CreateCompatibleBitmap = windll.gdi32.CreateCompatibleBitmap
# SelectObject = windll.gdi32.SelectObject
# BitBlt = windll.gdi32.BitBlt
# SRCCOPY = 0x00CC0020
# GetBitmapBits = windll.gdi32.GetBitmapBits
# DeleteObject = windll.gdi32.DeleteObject
# ReleaseDC = windll.user32.ReleaseDC
#
# # 排除缩放干扰
# windll.user32.SetProcessDPIAware()

# def capture(handle: HWND):
#     # 获取窗口客户区的大小
#     r = RECT()
#     GetClientRect(handle, byref(r))
#     width, height = r.right, r.bottom
#     # 开始截图
#     dc = GetDC(handle)
#     cdc = CreateCompatibleDC(dc)
#     bitmap = CreateCompatibleBitmap(dc, width, height)
#     SelectObject(cdc, bitmap)
#     BitBlt(cdc, 0, 0, width, height, dc, 0, 0, SRCCOPY)
#     # 截图是BGRA排列，因此总元素个数需要乘以4
#     total_bytes = width*height*4
#     buffer = bytearray(total_bytes)
#     byte_array = c_ubyte*total_bytes
#     GetBitmapBits(bitmap, total_bytes, byte_array.from_buffer(buffer))
#     DeleteObject(bitmap)
#     DeleteObject(cdc)
#     ReleaseDC(handle, dc)
#     # 返回截图数据为numpy.ndarray
#     return np.frombuffer(buffer, dtype=np.uint8).reshape(height, width, 4)
