import logging
import sys
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='[%(asctime)s]:[PYTHON]:%(message)s'
)

def chLog(message):
    print(message)
    logging.info(message)

if __name__ == '__main__':
    logging.debug
