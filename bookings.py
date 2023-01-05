from dataclasses import dataclass
from typing import Optional
from decimal import Decimal


@dataclass
class Booking:
    BookingID: Optional[int]
    Client: int
    Room: int
    Engineers: list[int]
    DaySessions: list[int]
    InitialCost: Decimal
    DiscountAmount: Decimal
    ActualCost: Decimal