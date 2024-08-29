from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Base, FoodModel
from core.food import Food

engine = create_engine('sqlite:///database/foods.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_food_to_db(food: Food):
    food_model = FoodModel(
        name=food.name,
        quantities=food.quantities,
        price=food.price,
        macros=food.macros,
        micros=food.micros,
        purchase_date=food.purchase_date,
        expiration_date=food.expiration_date,
        storage_conditions=food.storage_conditions,
        description=food.description
    )

    session.add(food_model)
    session.commit()
    return food_model
