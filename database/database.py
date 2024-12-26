from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, JSON

Base = declarative_base()


class ItemModel(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)

    food_details = relationship('FoodDetailsModel',
                                back_populates='product',
                                uselist=False,
                                cascade="all, delete-orphan")
    product_details = relationship('ProductDetailsModel',
                                   back_populates='product',
                                   uselist=False,
                                   cascade="all, delete-orphan")


class FoodDetailsModel(Base):
    __tablename__ = 'food_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantities = Column(JSON, nullable=False)
    macros = Column(JSON, nullable=False)
    micros = Column(JSON, nullable=False)
    storage_conditions = Column(String)

    product = relationship('ItemModel', back_populates='food_details')


class ProductDetailsModel(Base):
    __tablename__ = 'product_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    warranty_period = Column(String)
    power_consumption = Column(String)

    product = relationship('ItemModel', back_populates='product_details')


class ShoppingListModel(Base):
    __tablename__ = 'shopping_list'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)


engine = create_engine('sqlite:///database/database.db')
Session = sessionmaker(bind=engine)
session = Session()


def initialize_db():
    Base.metadata.create_all(engine)
