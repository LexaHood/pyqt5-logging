import sys, time, logging
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QProgressBar, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal


class Backend(QThread):
    dataChanged = pyqtSignal(str)
    finished = pyqtSignal(str)

    def __init__(self):
        self.activate = False
        super().__init__()

    def run(self):
        self.activate = True
        print(self.thread)
        while self.activate:
            print('111')
            time.sleep(1)

    def close(self):
        if (self.activate):
            self.activate = False
            print('closed')


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.back = Backend()

        self.btn_start = QPushButton('Start', self)
        self.btn_stop = QPushButton('Stop', self)
        self.pg = QProgressBar()
        self.setGeometry(300,250,200,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn_start)
        vbox.addWidget(self.btn_stop)
        vbox.addWidget(self.pg )
        self.setLayout(vbox)

    
        self.btn_start.clicked.connect(self.back.start)
        self.btn_stop.clicked.connect(self.back.close)


        self.ssssss()
        self.ssssss()
        self.ssssss()
        self.ssssss()

    def ssssss(self):
        if self.pg.value < 100:
            self.pg.setValue(self.pg.value + 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(main.exec_())