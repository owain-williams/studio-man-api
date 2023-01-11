from dataclasses import dataclass
from typing import Optional, Self
from decimal import Decimal
from db import update_booking, delete_booking
from datetime import datetime


@dataclass
class Booking:
    bookingid: Optional[int]
    client: int
    room: int
    engineers: Optional[list[int]]
    daySessions: Optional[list[int]]
    initialcost: Decimal
    discountamount: Decimal
    actualcost: Decimal
    paid: bool
    paiddate: datetime
    cancelled: bool

    def create(self) -> Self:
        '''Add or update the booking in the database.'''
        update_booking(self)
        return self

    def update(self) -> Self:
        '''Add or update the booking in the database.'''
        if self.bookingid is None:
            raise ValueError("BookingID must be set before updating")
        update_booking(self)
        return self

    def mark_as_paid(self) -> Self:
        '''Mark the booking as paid.'''
        self.paid = True
        self.paiddate = datetime.now()
        if self.bookingid is not None:
            update_booking(self)
        return self

    def cancel(self) -> Self:
        if self.bookingid is None:
            raise ValueError("BookingID must be set before cancelling")
        self.cancelled = True
        delete_booking(self)
        return self
