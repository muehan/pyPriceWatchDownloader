
from dataclasses import dataclass
import datetime

@dataclass
class Price:
    Id: str
    Price: float
    InsteadOfPrice: float
    Date: str
    Productid: str