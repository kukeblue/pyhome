from aip import AipOcr

APP_ID = '25713120'
API_KEY = 'GOkNrLxVH3cV8I7DVpXx67mh'
SECRET_KEY = '9MTEeMd2nNcm457CsGTGNV5ddkISAuI1'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


options = {"language_type": "CHN_ENG", "detect_direction": "false", "detect_language": "false", "probability": "false"}


def getImageText(path):
    image = get_file_content(path)
    return client.basicAccurate(image, options)
