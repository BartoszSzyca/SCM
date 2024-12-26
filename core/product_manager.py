from database.database import ProductDetailsModel, session


class ProductManager:
    @staticmethod
    def add_product_details_to_database(product_id, warranty_period,
                                        power_consumption):
        existing_product = session.query(ProductDetailsModel).filter_by(
            product_id=product_id).first()
        if existing_product:
            return "Product already exists"
        new_product = ProductDetailsModel(
            product_id=product_id,
            warranty_period=warranty_period,
            power_consumption=power_consumption,
        )
        session.add(new_product)
        session.commit()
        return "Product added successfully"

    def find_product_details(self, product_id):
        return session.query(ProductDetailsModel).filter_by(
            product_id=product_id).first()

    def update_product_details(self, product_id, warranty_period,
                               power_consumption):
        product = self.find_product_details(product_id)
        if product:
            product.warranty_period = warranty_period
            product.power_consumption = power_consumption
            session.commit()
        else:
            return "Product not found"
