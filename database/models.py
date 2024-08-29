from sqlalchemy import Column, Integer, Float, String, Date, JSON
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FoodModel(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantities = Column(JSON, nullable=False)
    price = Column(Float, default=0.0)
    macros = Column(JSON)
    micros = Column(JSON)
    purchase_date = Column(Date)
    expiration_date = Column(Date)
    storage_conditions = Column(String)
    description = Column(String)

    def __repr__(self):
        return (
            f"<FoodModel(id={self.id}, name={self.name}, quantities={self.quantities}, "
            f"price={self.price:.2f}, macros={self.macros}, micros={self.micros}, "
            f"purchase_date={self.purchase_date}, expiration_date={self.expiration_date}, "
            f"storage_conditions={self.storage_conditions}, description={self.description})>")
