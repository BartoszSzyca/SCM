from database.database import session, ShoppingListModel, ItemModel


class Core:
    def add_item(self, name, quantity=1):
        existing_item = session.query(ShoppingListModel).filter_by(name=name
                                                                   ).first()
        if existing_item:
            existing_item.quantity += quantity
        else:
            item = ShoppingListModel(name=name, quantity=quantity)
            session.add(item)
        session.commit()

    def add_item_from_product(self, product_name, quantity=1):
        product = session.query(ItemModel).filter_by(name=product_name).first()
        if product:
            self.add_item(product.name, quantity)
        else:
            print(f"Produkt '{product_name}' nie istnieje w bazie.")

    def get_items(self):
        return [(item.name, item.quantity) for item in session.query(
            ShoppingListModel).all()]

    def remove_item(self, name):
        item = session.query(ShoppingListModel).filter_by(name=name).first()
        if item:
            session.delete(item)
            session.commit()
