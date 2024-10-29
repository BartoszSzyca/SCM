from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.users import UsersBase
from database.food import FoodBase


users_engine = create_engine("sqlite:///database/users.db")
food_engine = create_engine("sqlite:///database/food.db")
user_data_engine = create_engine("sqlite:///database/user_data.db")

UsersBase.metadata.create_all(users_engine)
FoodBase.metadata.create_all(food_engine)

UsersSession = sessionmaker(bind=users_engine)
FoodSession = sessionmaker(bind=food_engine)

users_session = UsersSession()
food_session = FoodSession()