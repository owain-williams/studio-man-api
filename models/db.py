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

def createbooking(booking: Booking) -> Booking:
    '''Create a booking in the database.'''
    cursor.execute("INSERT INTO Bookings (Client, Room, Engineers, DaySessions, InitialCost, DiscountAmount, ActualCost) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (booking.Client, booking.Room, booking.Engineers, booking.DaySessions, booking.InitialCost, booking.DiscountAmount, booking.ActualCost))
    booking.BookingID = cursor.lastrowid
    return booking