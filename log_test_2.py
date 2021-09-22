import sys, time, logging, random
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QProgressBar, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal

def init_logger(name):
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)

    fh = logging.FileHandler(filename=f'test.log', mode="w")
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.INFO)

    logger.addHandler(sh)
    logger.addHandler(fh)
    logger.debug('logger was initialized')
# logging.basicConfig(format="%(message)s", level=logging.DEBUG)
init_logger("app")
logger = logging.getLogger("app.main")
#logger.debug('test')
# logging.getLogger('log_test_2.main')

class Backend(QThread):
    # dataChanged = pyqtSignal(str)
    # finished = pyqtSignal(str)
    bar = pyqtSignal()

    def __init__(self):
        self.activate = False
        super().__init__()

    def run(self):
        self.activate = True
        logger.info(self.thread)
        while self.activate:
            logger.info('working:...')
            hash = random.getrandbits(32)
            logger.debug(f'{hash}')
            time.sleep(1)
            logger.info(f'compilte!!!')
            self.bar.emit()

    def close(self):
        if (self.activate):
            self.activate = False
            logger.debug('closed')


class Window(QDialog):
    def __init__(self):
        super().__init__()

        logger.debug('app launched')

        self.back = Backend()

        self.btn_start = QPushButton('Start', self)
        self.btn_stop = QPushButton('Stop', self)
        self.pg = QProgressBar()
        self.setGeometry(300, 250, 200, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn_start)
        vbox.addWidget(self.btn_stop)
        vbox.addWidget(self.pg)
        self.setLayout(vbox)

        self.btn_start.clicked.connect(self.back.start)
        self.btn_stop.clicked.connect(self.back.close)
        self.back.bar.connect(self.pgroress_bar)
        # self.pgroress_bar()

    def pgroress_bar(self):
        # self.pg.setMaximum(4)
        self.pg.setValue(self.pg.value() + 1)
        logger.debug(f'progress: {self.pg.value()}')

        if self.pg.value() >= 100:
            self.back.close()


if __name__ == '__main__':
    # init_logger("app")
    # logger = logging.getLogger('aa.main')
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(main.exec_())