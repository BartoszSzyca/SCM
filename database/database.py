from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Base, FoodModel
from core.food import Food

engine = create_engine('sqlite:///database/foods.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_food_to_db(food: Food):
    existing_food = session.query(FoodModel).filter_by(name=food.name).first()

    if existing_food:
        print(f"Produkt o nazwie '{food.name}' już istnieje w bazie danych.")
        choice = input("Nadpisać go? (Y/N)")
        if choice.upper() == "Y":
            update_food_in_db(food, existing_food)
    else:
        food_model = FoodModel(
            name=food.name,
            quantities=food.quantities,
            price=food.price,
            macros=food.macros,
            micros=food.micros,
            purchase_date=food.purchase_date,
            expiration_date=food.expiration_date,
            storage_conditions=food.storage_conditions,
            description=food.description)

        session.add(food_model)
        session.commit()
        return food_model


def update_food_in_db(food: Food, existing_food):
    existing_food.quantities = food.quantities
    existing_food.price = food.price
    existing_food.macros = food.macros
    existing_food.micros = food.micros
    existing_food.purchase_date = food.purchase_date
    existing_food.expiration_date = food.expiration_date
    existing_food.storage_conditions = food.storage_conditions
    existing_food.description = food.description

    session.commit()
    print(f"Produkt o nazwie '{food.name}' został zaktualizowany.")
    return existing_food


def fetch_all_foods():
    foods = session.query(FoodModel).all()

    for food in foods:
        print(food)
