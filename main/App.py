import time
from sanic import Sanic
from sanic.response import json
from robot import Robot
from orjson import dumps
import ujson

app = Sanic("My Hello, world app", dumps=dumps)
myRobot = Robot()
myRobot.start()


@app.route('/api/test')
async def test(request):
    return json({'hello': 'world'})


@app.route('/api/mh/windowShot')
async def test(request):
    myRobot.mhWindow.resetMove()
    time.sleep(3)
    return json({'success': 'true'})


@app.route('/api/mh/getZgTask')
async def getZgTask(request):
    myRobot.mhWindow.resetMove()
    myRobot.mhWindow.doEvent('zgTask')
    return json({'success': 'true'})


@app.route('/api/mh/startServiceTjJJHS')
async def getZgTask(request):
    myRobot.mhWindow.resetMove()
    myRobot.mhWindow.userServices['zdJJHS'].status = 1
    return json({'success': 'true'})


@app.route('/api/mh/stopServiceTjJJHS')
async def getZgTask(request):
    myRobot.mhWindow.resetMove()
    myRobot.mhWindow.userServices['zdJJHS'].status = 0
    return json({'success': 'true'})


@app.route('/api/mh/getTaskAndEventStatus')
async def getTaskAndEventStatus(request):
    result = []
    for k, v in myRobot.mhWindow.userServices.items():
        result.append({'name': v.name, 'status': v.status, 'type': 'service'})
    for k, v in myRobot.mhWindow.userEvent.items():
        result.append({'name': v.name, 'status': v.status, 'type': 'event'})

    return json({'list': result})


if __name__ == '__main__':
    app.run(debug=False, access_log=False)
