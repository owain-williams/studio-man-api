# from dataclasses import dataclass
from typing import Optional, TypedDict
from decimal import Decimal
from db import createbooking

# @dataclass
class Booking:
    BookingID: Optional[int]
    Client: int
    Room: int
    Engineers: Optional[list[int]]
    DaySessions: Optional[list[int]]
    InitialCost: Decimal
    DiscountAmount: Decimal
    ActualCost: Decimal

    def commit(self) -> None:
        '''Add or update the booking in the database.'''
        createbooking(self)
        return self 
        
    
    def cancel(self):
        pass
    
    