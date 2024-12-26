from database.database import FoodDetailsModel, session


class FoodManager:

    def add_food_details_to_database(self, product_id, quantities, macros,
                                     micros, storage_conditions, **details):
        existing_food = session.query(FoodDetailsModel
                                      ).filter_by(product_id=product_id).first()
        if existing_food:
            return "Food already exists"
        new_food = FoodDetailsModel(
            product_id=product_id,
            quantities=quantities,
            macros=macros,
            micros=micros,
            storage_conditions=storage_conditions
        )
        session.add(new_food)
        session.commit()
        return "Food added successfully"

    def find_food_details(self, product_id):
        return session.query(FoodDetailsModel).filter_by(product_id=product_id
                                                         ).first()

    def update_food_details(self, food_id, quantities, macros,
                            micros, storage_conditions, **details):
        food = self.find_food_details(food_id)
        if food:
            food.quantities = quantities
            food.macros = macros
            food.micros = micros
            food.storage_conditions = storage_conditions
            session.commit()
        else:
            return "Food not found"
