from database.database import ItemModel, session
from core.food_manager import FoodManager
from core.product_manager import ProductManager


class ItemManager:

    def add_item_to_database(self, category, name, description, quantities,
                             macros, micros, storage_conditions,
                             warranty_period, power_consumption):
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
        if category == "food":
            FoodManager.add_food_details_to_database(
                product_id=new_item.id,
                quantities=quantities,
                macros=macros,
                micros=micros,
                storage_conditions=storage_conditions
            )
        elif category == "product":
            ProductManager.add_product_details_to_database(
                product_id=new_item.id,
                warranty_period=warranty_period,
                power_consumption=power_consumption
            )
        else:
            return "Unsuported category"

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
