from dataclasses import dataclass
from typing import Optional, Self
from decimal import Decimal
from db import update_booking, delete_booking
from datetime import datetime


@dataclass
class Booking:
    bookingid: Optional[int]
    client: int  # ClientID
    room: int  # RoomID
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


@dataclass
class FullDayBooking(Booking):
    pass


class PartDayBooking(Booking):
    start: datetime
    end: datetime

    def validate_times(self) -> None:
        if self.start >= self.end:
            raise ValueError("Start time must be before end time")
        if self.start.date() != self.end.date():
            raise ValueError("Start and end times must be on the same day")
