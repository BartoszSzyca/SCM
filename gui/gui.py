from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, \
    QPushButton, QListWidget, QLineEdit, QSpinBox, QTabWidget, QHBoxLayout
from SCM_testy.core.core import Core
from SCM_testy.core.products_core import ProductCore
from SCM_testy.database.database import initialize_db

# Inicjalizacja bazy danych
initialize_db()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.core = Core()
        self.product_core = ProductCore()
        self.setWindowTitle("Lista Zakupów")
        self.setGeometry(100, 100, 600, 400)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.init_shopping_list_tab()
        self.init_products_tab()

    def init_shopping_list_tab(self):
        shopping_tab = QWidget()
        layout = QVBoxLayout()

        # Tworzymy QHBoxLayout, aby umieścić obie listy obok siebie
        h_layout = QHBoxLayout()

        # Lista zakupów po lewej
        self.list_widget = QListWidget()
        h_layout.addWidget(self.list_widget)

        # Lista produktów po prawej
        self.shopping_list_product_widget = QListWidget()
        h_layout.addWidget(self.shopping_list_product_widget)

        layout.addLayout(
            h_layout)  # Dodajemy QHBoxLayout do głównego layoutu zakładki

        # Pole do dodawania przedmiotów do listy zakupów
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

        # Dodajemy przycisk do ukrywania/pokazywania prawej listy
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

        # Dodatkowe pola dla żywności
        self.food_quantities_input = QLineEdit()
        self.food_quantities_input.setPlaceholderText(
            "Ilości (JSON: {'kg': 1})")
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

        # Dodatkowe pola dla Product
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
        self.tabs.addTab(products_tab, "Produkty")

    def toggle_shopping_list(self):
        # Zmiana widoczności prawej listy
        current_visibility = self.shopping_list_product_widget.isVisible()
        self.shopping_list_product_widget.setVisible(not current_visibility)

    def refresh_list(self):
        self.list_widget.clear()
        for name, quantity in self.core.get_items():
            self.list_widget.addItem(f"{name} (Ilość: {quantity})")

    def refresh_products(self):
        # Odświeżanie listy produktów w zakładce "Produkty"
        self.product_list_widget.clear()
        for product in self.product_core.get_products():
            self.product_list_widget.addItem(
                f"{product.name} - {product.description or 'Brak opisu'}")

        # Odświeżanie listy dostępnych produktów w zakładce "Lista Zakupów"
        self.shopping_list_product_widget.clear()
        for product in self.product_core.get_products():
            self.shopping_list_product_widget.addItem(
                f"{product.name} - {product.description or 'Brak opisu'}")

    def add_item(self):
        name = self.input_field.text()
        quantity = self.quantity_input.value()
        if name:
            self.core.add_item(name, quantity)
            self.refresh_list()

    def add_item_from_product(self):
        selected_items = self.shopping_list_product_widget.selectedItems()  # Zmieniona nazwa zmiennej
        quantity = self.quantity_input.value()
        for item in selected_items:
            product_name = item.text().split(" - ")[0]
            self.core.add_item_from_product(product_name, quantity)
            self.refresh_list()

    def remove_item(self):
        selected_items = self.list_widget.selectedItems()
        for item in selected_items:
            name = item.text().split(" (")[0]
            self.core.remove_item(name)
            self.refresh_list()

    def add_product(self):
        category = self.product_category_input.text()
        name = self.product_name_input.text()
        description = self.product_description_input.text()

        if category == 'food':
            quantities = eval(self.food_quantities_input.text())
            macros = eval(self.food_macros_input.text())
            micros = eval(self.food_micros_input.text())
            storage_conditions = self.food_storage_input.text()
            self.product_core.add_food(name, description, quantities, macros,
                                       micros, storage_conditions)

        elif category == 'product':
            warranty_period = self.product_warranty_input.text()
            power_consumption = self.product_power_input.text()
            self.product_core.add_product(name, description, warranty_period,
                                          power_consumption)

        self.refresh_products()

    def delete_product(self):
        selected_items = self.product_list_widget.selectedItems()
        if selected_items:
            product_name = selected_items[0].text().split(" - ")[0]
            self.product_core.delete_product(product_name)
            self.refresh_products()  # Odśwież listę po usunięciu

    def edit_product(self):
        selected_items = self.product_list_widget.selectedItems()
        if selected_items:
            product_name = selected_items[0].text().split(" - ")[0]
            product = self.product_core.find_product(product_name)

            if product:
                self.product_name_input.setText(product.name)
                self.product_description_input.setText(product.description)

                if product.category == 'food':
                    food_details = self.product_core.get_food_details(
                        product.id)
                    if food_details:
                        self.food_quantities_input.setText(
                            str(food_details.quantities))
                        self.food_macros_input.setText(str(food_details.macros))
                        self.food_micros_input.setText(str(food_details.micros))
                        self.food_storage_input.setText(
                            food_details.storage_conditions)

                elif product.category == 'product':
                    product_details = self.product_core.get_product_details(
                        product.id)
                    if product_details:
                        self.product_warranty_input.setText(
                            product_details.warranty_period)
                        self.product_power_input.setText(
                            product_details.power_consumption)

    def save_product_changes(self):
        selected_items = self.product_list_widget.selectedItems()
        if selected_items:
            product_name = selected_items[0].text().split(" - ")[0]
            product = self.product_core.find_product(product_name)

            if product:
                new_name = self.product_name_input.text()
                new_description = self.product_description_input.text()

                self.product_core.edit_product(product_name, new_name,
                                               new_description)

                if product.category == 'food':
                    quantities = eval(self.food_quantities_input.text())
                    macros = eval(self.food_macros_input.text())
                    micros = eval(self.food_micros_input.text())
                    storage_conditions = self.food_storage_input.text()
                    self.product_core.update_food_details(product.id,
                                                          quantities, macros,
                                                          micros,
                                                          storage_conditions)

                elif product.category == 'product':
                    warranty_period = self.product_warranty_input.text()
                    power_consumption = self.product_power_input.text()
                    self.product_core.update_product_details(product.id,
                                                             warranty_period,
                                                             power_consumption)

                self.refresh_products()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
