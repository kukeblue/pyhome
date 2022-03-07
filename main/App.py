import time
from sanic import Sanic
from sanic.response import json
from robot import Robot
from cnocr import CnOcr
from cnstd import CnStd
import pyautogui

app = Sanic("My Hello, world app")
app.static('/', '../static')
app.static('/', '../static/index.html')
myRobot = Robot()
myRobot.start()


@app.route('/api/mh/windowShot')
async def test(request):
    myRobot.mhWindow.resetMove()
    time.sleep(3)
    return json({'success': 'true'})


@app.route('/api/mh/getZgTask')
async def getZgTask(request):

    if myRobot.mhWindow.userEvent.get('zgTask').instance is not None:
        if myRobot.mhWindow.userEvent.get('zgTask').instance.status == 1:
            myRobot.mhWindow.userEvent.get('zgTask').instance.status = 2
        if myRobot.mhWindow.userEvent.get('zgTask').instance.status == -1:
            myRobot.mhWindow.userEvent.get('zgTask').instance.status = 2
    else:
        myRobot.mhWindow.resetMove2()
        myRobot.mhWindow.doEvent('zgTask')
        myRobot.mhWindow.userEvent.get('zgTask').instance.status = 2
    return json({'success': 'true'})


@app.route('/api/mh/stopZgTask')
async def stopZgTask(request):
    if myRobot.mhWindow.userEvent.get('zgTask').instance is not None:
        myRobot.mhWindow.userEvent.get('zgTask').instance.status = -1

    return json({'success': 'true'})


@app.route('/api/mh/startServiceTjJJHS')
async def startServiceTjJJHS(request):
    myRobot.mhWindow.resetMove()
    myRobot.mhWindow.userServices['zdJJHS'].status = 1
    return json({'success': 'true'})


@app.route('/api/mh/stopServiceTjJJHS')
async def stopServiceTjJJHS(request):
    myRobot.mhWindow.resetMove()
    myRobot.mhWindow.stopService('zdJJHS')
    return json({'success': 'true'})

@app.route('/api/mh/serviceTjMSZY')
async def stopServiceTjJJHS(request):
    if  myRobot.mhWindow.userServices['zdMSZY'].status == 0:
        myRobot.mhWindow.userServices['zdMSZY'].status = 1
    else:
        myRobot.mhWindow.userServices['zdMSZY'].status = 0
    return json({'success': 'true'})


@app.route('/api/mh/getTaskAndEventStatus')
async def getTaskAndEventStatus(request):
    result = []
    for k, v in myRobot.mhWindow.userServices.items():
        result.append({'name': v.name, 'status': v.status, 'type': 'service'})
    for k, v in myRobot.mhWindow.userEvent.items():
        status = 0
        if v.instance is not None and v.instance.status > 0:
            status = v.instance.status

        result.append({'name': v.name, 'status': status, 'type': 'event'})

    return json({'list': result})


@app.route('/api/test')
async def test(request):
    print('test')
    # myRobot.mhWindow.windowShot()
    std = CnStd()
    cn_ocr = CnOcr(cand_alphabet='的签到答题')
    box_infos = std.detect('temp/1.png')
    for box_info in box_infos['detected_texts']:
        cropped_img = box_info['cropped_img']
        ocr_res = cn_ocr.ocr_for_single_line(cropped_img)
        print('ocr result: %s' % str(ocr_res))
    return json({'success': True})


@app.route('/test')
async def test(request):
    print('test')
    # myRobot.mhWindow.windowShot()
    std = CnStd()
    cn_ocr = CnOcr(cand_alphabet='的签到答题')
    box_infos = std.detect('temp/1.png')
    for box_info in box_infos['detected_texts']:
        cropped_img = box_info['cropped_img']
        ocr_res = cn_ocr.ocr_for_single_line(cropped_img)
        print('ocr result: %s' % str(ocr_res))
    return json({'success': True})


if __name__ == '__main__':
    app.run(debug=False, access_log=False)
