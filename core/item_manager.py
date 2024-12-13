from database import session, ItemModel


class ItemManager:

    def add_item_to_database(self, category, name, description):
        existing_item = self.find_item_in_database(name)
        if existing_item:
            return "Item already exists"
        new_item = ItemModel(
            category=category,
            name=name,
            description=description,
        )
        session.add(new_item)
        session.commit()
        return "Item added successfully"

    def get_all_items_from_database(self):
        return session.query(ItemModel).all()

    def remove_item_from_database(self, item_name):
        item = self.find_item_in_database(item_name)
        if item:
            session.delete(item)
            session.commit()
            return "Item removed successfully"
        return "Cannot remove item. item does not exist."

    def find_item_in_database(self, item_name):
        return session.query(ItemModel).filter_by(name=item_name).first()


    def update_item_in_database(self, item_name, category, name, description):
        item = self.find_item_in_database(item_name)
        if item:
            item.category = category
            item.name = name
            item.description = description
            session.commit()
        else:
            return "Item not found"
