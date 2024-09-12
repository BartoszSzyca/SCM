from PySide6.QtWidgets import QApplication
from gui.start_screen import StartScreen
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StartScreen()
    window.show()

    app.exec()