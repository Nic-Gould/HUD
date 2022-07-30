# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt5 import QApplication, QWidget
from PyQt5.QtCore import QFile
from PyQt5.QtUiTools import QUiLoader

class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
