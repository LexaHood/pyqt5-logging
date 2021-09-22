import logging
from mod.mod_test import Objk

def init_log(name):
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)

    fh = logging.FileHandler(filename=f'test.log')
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.DEBUG)

    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug('logger was initialized')


if __name__ == '__main__':
    init_log("app")
    logger = logging.getLogger("app.main")
    o = Objk
    o.work()