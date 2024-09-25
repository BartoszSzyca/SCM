from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("SCM")

        menu_bar = self.menuBar()
        window_menu = menu_bar.addMenu("File")
        food_list_menu = menu_bar.addMenu("Food")

        logout_actrion = window_menu.addAction("Logout")
        logout_actrion.triggered.connect(self.logout_app)

    def logout_app(self):
        self.app.quit()

