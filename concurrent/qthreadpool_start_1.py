import sys
import time

from PySide6.QtCore import QThreadPool, QTimer, Slot
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads"
            % self.threadpool.maxThreadCount()
        )

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    # tag::do_some_work[]
    def oh_no(self):
        self.threadpool.start(self.do_some_work)

    @Slot()
    def do_some_work(self):
        print("Thread start")
        time.sleep(5)
        print("Thread complete")

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

    # end::do_some_work[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
