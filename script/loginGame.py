# coding:utf-8
import time
from win32com.client import Dispatch
import win32api
import utils
import sys

op = Dispatch("op.opsoft")


def login(accounts):
    win32api.ShellExecute(0, 'open',
                          r'C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\梦幻西游',
                          '', '', 1)
    while True:
        print('login game start')
        time.sleep(1)
        hwnd = op.findWindow('', '梦幻西游 ONLINE')
        if hwnd is not None and hwnd != 0:
            time.sleep(3)
            ret = op.FindMultiColor(1157, 681, 1245, 760, '5f26a0-993d27', '7|0|5e229e', 0.95, 0)
            print(ret)
            if ret[0] > 0:
                op.MoveTo(1208, 724)
                time.sleep(1)
                op.LeftClick()
            break
        else:
             print('not find window')
             return
    for index in range(len(accounts)):
        account = accounts[index]
        while True:
            time.sleep(1)
            # 点击下一步
            print('info:click next')
            ret2 = op.FindMultiColor(1282, 844, 1416, 899, 'c0d8f0-993d27', '0|-1|c0d8f0', 0.95, 0)
            if ret2[0] > 0:
                op.MoveTo(1352, 871)
                time.sleep(1)
                op.LeftClick()
                break

        while True:
            time.sleep(1)
            print('info:click login')
            ret2 = op.FindColor(899, 516, 994, 543, 'd8d8a8-993d27', 0.95, 0)
            if ret2[0] > 0:
                print('info:enter username')
                op.MoveTo(1035, 599)
                op.LeftClick()
                print('info:delete old username')
                for num in range(0, 20):
                    op.KeyPress('37')
                for num in range(0, 20):
                    op.KeyPress('46')
                print('info:enter new username')
                utils.writeText(account["username"])
                time.sleep(1)
                op.MoveTo(1045, 629)
                op.LeftClick()
                time.sleep(1)
                utils.writeText(account["password"])
                time.sleep(1)
                op.MoveTo(1145, 771)
                op.LeftClick()
                break

        while True:
            print('info:click next button')
            time.sleep(1)
            op.LeftClick()
            ret2 = op.FindColor(1281, 842, 1408, 898, 'c8d0d0-993d27', 0.95, 0)
            if ret2[0] > 0:
                op.MoveTo(1356, 875)
                op.LeftClick()
                break

        while True:
            print('info:click enter game')
            time.sleep(1)
            ret2 = op.FindMultiColor(671, 836, 735, 864, 'a0b0d0-993d27', '2|6|90a4d0,4|0|8898b8', 0.95, 0)
            if ret2[0] > 0:
                op.MoveTo(1335, 879)
                op.LeftClick()
                time.sleep(2)
                op.MoveTo(979, 528)
                op.LeftClick()
                break

        while True:
            print('info:enter code')
            time.sleep(1)
            code = utils.getGameVerificationCode()
            if code is not None:
                utils.writeText(code)
                op.MoveTo(982, 629)
                op.LeftClick()
                break

        while True:
            print('is login success?')
            time.sleep(1)
            ret2 = op.FindColor(641, 340, 657, 355, '185878-993d27|084060-000000|78e4e0-000000', 0.90, 0)
            if ret2[0] > 0:
                print('login success！')
                break

        if index + 1 != len(accounts):
            print('next account')
            ret2 = op.FindMultiColor(771, 297, 1444, 319, '3e5c72-993d27', '0|-4|3f6d8e,3|-3|9cb0c5', 0.95, 0)
            if ret2[0] > 0:
                op.MoveTo(ret2[1], ret2[2])
                op.LeftClick()
            else:
                print('finish')


accountMap = {
    "ch1993com1": "wg520201314wg",
    "ch1993com2": "wg520201314wg",
    "ch1993com3": "wg520201314wg",
    "ch1993com4": "520201314wgg",
    "ch1993com5": "wg520201314wg",
    "ch1993com6": "wg520201314wg",
    "ch1993com7": "wg520201314wg",
    "ch1993com8": "wg520201314wgG",
    "ch.1993.com": "520201314wgg",
    "mm1042061794": "520201314wgg",
}

if __name__ == "__main__":
    args = sys.argv[1:]
    print(args)
    print(len(args))
    Accounts = []
    for index in range(len(args)):
       Accounts.append({"username": args[index], "password": accountMap[args[index]]})
    print(Accounts)
    login(Accounts)
