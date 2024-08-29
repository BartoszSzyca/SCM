from typing import Dict, Optional, Union
from datetime import date

class Food:
    def __init__(self, name: str, quantities: Dict[str, Union[int, float]], price: float = 0.0, 
                 macros: Optional[Dict[str, float]] = None, micros: Optional[Dict[str, float]] = None,
                 purchase_date: Optional[date] = None, expiration_date: Optional[date] = None, 
                 storage_conditions: Optional[str] = None, description: Optional[str] = None):

        self.name = name
        self.quantities = quantities
        self.price = price
        self.macros = macros if macros is not None else {}
        self.micros = micros if micros is not None else {}
        self.purchase_date = purchase_date
        self.expiration_date = expiration_date
        self.storage_conditions = storage_conditions
        self.description = description
