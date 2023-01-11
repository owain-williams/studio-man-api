from dotenv import dotenv_values
import mysql.connector
from bookings import Booking

db_config = dotenv_values(".env")

db = mysql.connector.connect(
    host=db_config["HOST"],
    user=db_config["USER"],
    password=db_config["PASSWORD"],
    database=db_config["DATABASE"]
)

cursor = db.cursor()


def update_booking(booking: Booking) -> Booking:
    '''Create a booking in the database.'''
    if booking.bookingid is None:
        cursor.execute("INSERT INTO Bookings (Client, Room, Engineers, DaySessions, InitialCost, DiscountAmount, ActualCost) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (booking.client, booking.room, booking.engineers, booking.daySessions, booking.initialcost, booking.discountamount, booking.actualcost))
        booking.bookingid = cursor.lastrowid
        print(f'Booking created with ID {booking.bookingid}')
    else:
        cursor.execute("UPDATE Bookings SET Client = %s, Room = %s, Engineers = %s, DaySessions = %s, InitialCost = %s, DiscountAmount = %s, ActualCost = %s WHERE BookingID = %s",
                       (booking.client, booking.room, booking.engineers, booking.daySessions, booking.initialcost, booking.discountamount, booking.actualcost, booking.bookingid))
        print(f'Booking updated with ID {booking.bookingid}')
    return booking


def delete_booking(booking: Booking) -> None:
    '''Delete a booking from the database.'''
    cursor.execute("DELETE FROM Bookings WHERE BookingID = %s",
                   (booking.bookingid,))
