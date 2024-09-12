from sqlalchemy import Column, Integer, Float, String, Date, JSON, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class FoodModel(Base):
    __tablename__ = 'foods'

    food_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    quantities = Column(JSON, nullable=False)
    macros = Column(JSON, nullable=False)
    micros = Column(JSON, nullable=False)
    storage_conditions = Column(String)
    description = Column(String)

    def __repr__(self):
        return (
            f"<FoodModel(food_id={self.food_id}, "
            f"name={self.name}, "
            f"quantities={self.quantities}, "
            f"macros={self.macros}, "
            f"micros={self.micros}, "
            f"storage_conditions={self.storage_conditions}, "
            f"description={self.description})>")

    def __str__(self):
        return f"{self.name} ({self.food_id})"


class FridgeModel(Base):
    __tablename__ = 'fridge'

    food_id = Column(Integer, ForeignKey('foods.food_id'), nullable=False)
    quantities = Column(Integer, nullable=False)
    purchase_date = Column(Date)
    expiration_date = Column(Date)

    food = relationship("FoodModel", backref="fridge_items")

    def __repr__(self):
        return (f"<FridgeModel(food_id={self.food_id}, "
                f"name={self.food.name}, "
                f"quantities={self.quantities}, "
                f"purchase_date={self.purchase_date}, "
                f"expiration_date={self.expiration_date}, "
                f"storage_conditions={self.food.storage_conditions}, "
                f"description={self.food.description})>")

    def __str__(self):
        return f"Fridge item for {self.food.name} with {self.quantities} units"


class ShoppingListModel(Base):
    __tablename__ = 'shopping_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    food_id = Column(Integer, ForeignKey('foods.food_id'), nullable=False)
    quantities = Column(Integer, nullable=False)
    price = Column(Float)

    food = relationship("FoodModel", backref="shopping_list_items")

    def __repr__(self):
        return (f"<ShoppingListModel(id={self.id}, "
                f"food_id={self.food_id}, "
                f"quantities={self.quantities}, "
                f"price={self.price:.2f})>")

    def __str__(self):
        return (f"Shopping list item: {self.food.name}, "
                f"Quantity: {self.quantities}, "
                f"Price: {self.price:.2f}")
