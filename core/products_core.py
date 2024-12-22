from SCM_testy.database.database import session, ItemModel, FoodDetailsModel, \
    ProductDetailsModel


class ProductCore:

    def add_food(self, name, description, quantities, macros, micros,
                 storage_conditions):
        product = ItemModel(name=name, category='food',
                               description=description)
        session.add(product)
        session.flush()  # Potrzebne, aby uzyskać ID produktu przed dodaniem szczegółów

        food_details = FoodDetailsModel(
            product_id=product.id,
            quantities=quantities,
            macros=macros,
            micros=micros,
            storage_conditions=storage_conditions
        )
        session.add(food_details)
        session.commit()

    def add_product(self, name, description, warranty_period,
                    power_consumption):
        product = ItemModel(name=name, category='product',
                               description=description)
        session.add(product)
        session.flush()

        product_details = ProductDetailsModel(
            product_id=product.id,
            warranty_period=warranty_period,
            power_consumption=power_consumption
        )
        session.add(product_details)
        session.commit()

    def get_products(self):
        return session.query(ItemModel).all()

    def get_food_details(self, product_id):
        return session.query(FoodDetailsModel).filter_by(
            product_id=product_id).first()

    def get_product_details(self, product_id):
        return session.query(ProductDetailsModel).filter_by(
            product_id=product_id).first()

    def find_product(self, name):
        return session.query(ItemModel).filter_by(name=name).first()

    def delete_product(self, product_name):
        product = session.query(ItemModel).filter(
            ItemModel.name == product_name).first()
        if product:
            session.delete(product)
            session.commit()

    def edit_product(self, product_name, new_name, new_description):
        product = session.query(ItemModel).filter(
            ItemModel.name == product_name).first()
        if product:
            product.name = new_name
            product.description = new_description
            session.commit()

    def update_food_details(self, product_id, quantities, macros, micros,
                            storage_conditions):
        food_details = session.query(FoodDetailsModel).filter_by(
            product_id=product_id).first()
        if food_details:
            food_details.quantities = quantities
            food_details.macros = macros
            food_details.micros = micros
            food_details.storage_conditions = storage_conditions
            session.commit()

    def update_product_details(self, product_id, warranty_period,
                               power_consumption):
        product_details = session.query(ProductDetailsModel).filter_by(
            product_id=product_id).first()
        if product_details:
            product_details.warranty_period = warranty_period
            product_details.power_consumption = power_consumption
            session.commit()
