from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6 import uic, QtGui
import sys
import os
import modules.cccd as cccd

CONFIG_FILE = 'path.txt'


class Tools(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tools.ui', self)
        self.show()
        self.select_cccd_button.clicked.connect(self.process)
        self.last_path = self.load_last_path()

    def load_last_path(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return f.read().strip()

    def save_last_path(self, path):
        with open(CONFIG_FILE, 'w') as f:
            f.write(path)

    def process(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            'Open files',
            self.last_path,
            "Images (*.jpg *.png *.jpeg *.gif)"
        )
        if file_paths:
            self.save_last_path(os.path.dirname(file_paths[-1]))

            for path in file_paths:
                cccd.process(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.ico'))
    tools = Tools()
    app.exec()