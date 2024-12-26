from PySide6.QtWidgets import QApplication
from gui.gui import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = StartScreen()
    window = MainWindow()
    window.show()

    app.exec()
