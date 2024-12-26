from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, \
    QListWidget, QLineEdit, QSpinBox, QTabWidget, QHBoxLayout
from core.core import Core
from database.database import initialize_db
from core.item_manager import ItemManager
from core.food_manager import FoodManager
from core.product_manager import ProductManager

initialize_db()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.core = Core()
        self.item_manager = ItemManager()
        self.food_manager = FoodManager()
        self.product_manager = ProductManager()
        self.setWindowTitle("Lista Zakupów")
        self.setGeometry(100, 100, 600, 400)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.init_shopping_list_tab()
        self.init_products_tab()

    def init_shopping_list_tab(self):
        shopping_tab = QWidget()
        layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        self.list_widget = QListWidget()
        h_layout.addWidget(self.list_widget)

        self.shopping_list_product_widget = QListWidget()
        h_layout.addWidget(self.shopping_list_product_widget)

        layout.addLayout(h_layout)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Wpisz nazwę przedmiotu")
        layout.addWidget(self.input_field)

        self.quantity_input = QSpinBox()
        self.quantity_input.setMinimum(1)
        self.quantity_input.setValue(1)
        self.quantity_input.setPrefix("Ilość: ")
        layout.addWidget(self.quantity_input)

        self.add_button = QPushButton("Dodaj")
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Usuń")
        self.remove_button.clicked.connect(self.remove_item)
        layout.addWidget(self.remove_button)

        self.product_add_button = QPushButton("Dodaj z Produktów")
        self.product_add_button.clicked.connect(self.add_item_from_product)
        layout.addWidget(self.product_add_button)

        self.toggle_button = QPushButton("Ukryj/Pokaż Listę Produktów")
        self.toggle_button.clicked.connect(self.toggle_shopping_list)
        layout.addWidget(self.toggle_button)

        self.refresh_list()

        shopping_tab.setLayout(layout)
        self.tabs.addTab(shopping_tab, "Lista Zakupów")

    def init_products_tab(self):
        products_tab = QWidget()
        layout = QVBoxLayout()

        self.product_category_input = QLineEdit()
        self.product_category_input.setPlaceholderText(
            "Kategoria: 'food' lub 'product'")
        layout.addWidget(self.product_category_input)

        self.product_name_input = QLineEdit()
        self.product_name_input.setPlaceholderText("Nazwa produktu")
        layout.addWidget(self.product_name_input)

        self.product_description_input = QLineEdit()
        self.product_description_input.setPlaceholderText("Opis produktu")
        layout.addWidget(self.product_description_input)

        self.food_quantities_input = QLineEdit()
        self.food_quantities_input.setPlaceholderText("Ilości (JSON: {'kg': 1})"
                                                      )
        layout.addWidget(self.food_quantities_input)

        self.food_macros_input = QLineEdit()
        self.food_macros_input.setPlaceholderText("Makroskładniki (JSON)")
        layout.addWidget(self.food_macros_input)

        self.food_micros_input = QLineEdit()
        self.food_micros_input.setPlaceholderText("Mikroskładniki (JSON)")
        layout.addWidget(self.food_micros_input)

        self.food_storage_input = QLineEdit()
        self.food_storage_input.setPlaceholderText("Warunki przechowywania")
        layout.addWidget(self.food_storage_input)

        self.product_warranty_input = QLineEdit()
        self.product_warranty_input.setPlaceholderText("Okres gwarancji")
        layout.addWidget(self.product_warranty_input)

        self.product_power_input = QLineEdit()
        self.product_power_input.setPlaceholderText("Zużycie energii")
        layout.addWidget(self.product_power_input)

        self.add_product_button = QPushButton("Dodaj Produkt")
        self.add_product_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_product_button)

        self.delete_product_button = QPushButton("Usuń Produkt")
        self.delete_product_button.clicked.connect(self.delete_product)
        layout.addWidget(self.delete_product_button)

        self.edit_product_button = QPushButton("Edytuj Produkt")
        self.edit_product_button.clicked.connect(self.edit_product)
        layout.addWidget(self.edit_product_button)

        self.save_changes_button = QPushButton("Zapisz zmiany")
        self.save_changes_button.clicked.connect(self.save_product_changes)
        layout.addWidget(self.save_changes_button)

        self.product_list_widget = QListWidget()
        layout.addWidget(self.product_list_widget)

        self.refresh_products()
        products_tab.setLayout(layout)
        self.tabs.addTab(products_tab, "Baza Produktów")

    def toggle_shopping_list(self):
        current_visibility = self.shopping_list_product_widget.isVisible()
        self.shopping_list_product_widget.setVisible(not current_visibility)

    def refresh_list(self):
        # shopinglist
        self.list_widget.clear()
        for name, quantity in self.core.get_items():
            self.list_widget.addItem(f"{name} (Ilość: {quantity})")

    def refresh_products(self):
        self.product_list_widget.clear()
        for product in self.item_manager.get_all_items_from_database():
            self.product_list_widget.addItem(
                f"{product.name} - {product.description or 'Brak opisu'}")

        self.shopping_list_product_widget.clear()
        for product in self.item_manager.get_all_items_from_database():
            self.shopping_list_product_widget.addItem(
                f"{product.name} - {product.description or 'Brak opisu'}")

    def add_item(self):
        # shopinglist
        name = self.input_field.text()
        quantity = self.quantity_input.value()
        if name:
            self.core.add_item(name, quantity)
            self.refresh_list()

    def add_item_from_product(self):
        # shopinglist
        selected_items = self.shopping_list_product_widget.selectedItems()
        quantity = self.quantity_input.value()
        for item in selected_items:
            product_name = item.text().split(" - ")[0]
            self.core.add_item_from_product(product_name, quantity)
            self.refresh_list()

    def remove_item(self):
        # shopinglist
        selected_items = self.list_widget.selectedItems()
        for item in selected_items:
            name = item.text().split(" (")[0]
            self.core.remove_item(name)
            self.refresh_list()

    def add_product(self):
        item_data = {"category": self.product_category_input.text(),
                     "name": self.product_name_input.text(),
                     "description": self.product_description_input.text(),
                     "quantities": self.food_quantities_input.text(),
                     "macros": self.food_macros_input.text(),
                     "micros": self.food_micros_input.text(),
                     "storage_conditions": self.food_storage_input.text(),
                     "warranty_period": self.product_warranty_input.text(),
                     "power_consumption": self.product_power_input.text()
                     }
        self.item_manager.add_item_to_database(**item_data)
        self.refresh_products()

    def delete_product(self):
        selected_items = self.product_list_widget.selectedItems()
        if selected_items:
            product_name = selected_items[0].text().split(" - ")[0]
            self.item_manager.remove_item_from_database(product_name)
            self.refresh_products()

    def edit_product(self):
        selected_items = self.product_list_widget.selectedItems()
        if selected_items:
            product_name = selected_items[0].text().split(" - ")[0]
            product = self.item_manager.find_item_in_database(product_name)

            if product:
                self.product_name_input.setText(product.name)
                self.product_description_input.setText(product.description)

                if product.category == 'food':
                    food_details = self.food_manager.find_food_details(
                        product.id)
                    if food_details:
                        self.product_category_input.setText('food')
                        self.food_quantities_input.setText(
                            str(food_details.quantities))
                        self.food_macros_input.setText(str(food_details.macros))
                        self.food_micros_input.setText(str(food_details.micros))
                        self.food_storage_input.setText(
                            food_details.storage_conditions)
                        self.product_warranty_input.setText("")
                        self.product_power_input.setText("")

                elif product.category == 'product':
                    product_details = self.product_manager.find_product_details(
                        product.id)
                    if product_details:
                        self.product_category_input.setText('product')
                        self.food_quantities_input.setText("")
                        self.food_macros_input.setText("")
                        self.food_micros_input.setText("")
                        self.food_storage_input.setText("")
                        self.product_warranty_input.setText(
                            product_details.warranty_period)
                        self.product_power_input.setText(
                            product_details.power_consumption)

    def save_product_changes(self):
        selected_items = self.product_list_widget.selectedItems()
        if selected_items:
            product_name = selected_items[0].text().split(" - ")[0]
            product = self.item_manager.find_item_in_database(product_name)

            if product:
                new_name = self.product_name_input.text()
                new_description = self.product_description_input.text()
                new_category = self.product_description_input.text()

                self.item_manager.update_item_in_database(product_name,
                                                          new_category,
                                                          new_name,
                                                          new_description)

                if product.category == 'food':
                    quantities = eval(self.food_quantities_input.text())
                    macros = eval(self.food_macros_input.text())
                    micros = eval(self.food_micros_input.text())
                    storage_conditions = self.food_storage_input.text()
                    self.food_manager.update_food_details(product.id,
                                                          quantities, macros,
                                                          micros,
                                                          storage_conditions)

                elif product.category == 'product':
                    warranty_period = self.product_warranty_input.text()
                    power_consumption = self.product_power_input.text()
                    self.product_manager.update_product_details(product.id,
                                                                warranty_period,
                                                                power_consumption)

        self.refresh_products()
