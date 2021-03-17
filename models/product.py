
from dataclasses import dataclass
import datetime

@dataclass
class Product:
    id: str
    Producttypeid: str
    Productid: str
    ProductidAsString: str
    Name: str
    Fullname: float
    SimpleName: float
    Date: datetime.datetime
