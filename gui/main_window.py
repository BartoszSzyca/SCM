from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTableWidget, \
    QTableWidgetItem
from database.database import fetch_all_foods


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

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Nazwa", "Ilości", "Makroskładniki", "Mikroskładniki",
             "Warunki przechowywania"])
        layout.addWidget(self.table)

        self.populate_food_list()

    def populate_food_list(self):
        foods = fetch_all_foods()
        self.table.setRowCount(len(foods))

        for row, food in enumerate(foods):
            self.table.setItem(row, 0, QTableWidgetItem(str(food.food_id)))
            self.table.setItem(row, 1, QTableWidgetItem(food.name))
            self.table.setItem(row, 2, QTableWidgetItem(str(food.quantities)))
            self.table.setItem(row, 3, QTableWidgetItem(str(food.macros)))
            self.table.setItem(row, 4, QTableWidgetItem(str(food.micros)))
            self.table.setItem(row, 5,
                               QTableWidgetItem(food.storage_conditions))

    def logout_app(self):
        self.app.quit()
