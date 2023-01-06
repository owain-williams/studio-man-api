from dataclasses import dataclass
from typing import Optional
from decimal import Decimal
from db import db

cursor = db.cursor()


@dataclass
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
        if self.BookingID is None:
            cursor.execute("INSERT INTO Bookings (Client, Room, Engineers, DaySessions, InitialCost, DiscountAmount, ActualCost) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (self.Client, self.Room, self.Engineers, self.DaySessions, self.InitialCost, self.DiscountAmount, self.ActualCost))
            db.commit()
            self.BookingID = cursor.lastrowid
            print(f'Booking created. ID: {self.BookingID}')        
        
    
    def cancel(self):
        pass
    
    