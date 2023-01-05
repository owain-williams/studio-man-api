from dataclasses import dataclass
from typing import Optional
from db import db
from decimal import Decimal

cursor = db.cursor()


@dataclass
class Engineer:
    EngineerID: Optional[int]
    FirstName: str
    LastName: str
    Rate: Decimal

    def setrate(self, rate: Decimal) -> None:
        '''Set the engineer's rate.'''
        cursor.execute("UPDATE Engineers SET Rate=%s WHERE EngineerID=%s",
                       (rate, self.EngineerID))
        db.commit()
        self.Rate = Decimal(rate)
        print(f'Engineer {self.FirstName} {self.LastName} rate set to {rate}')

    def commit(self) -> None:
        '''Add or update the engineer in the database.'''
        if self.EngineerID is None:
            cursor.execute(
                "INSERT INTO Engineers (FirstName, LastName, Rate) VALUES (%s, %s, %s)",
                (self.FirstName, self.LastName, self.Rate)
            )
            db.commit()
            self.EngineerID = cursor.lastrowid
            print(
                f'Engineer "{self.FirstName} {self.LastName}" created. ID: {self.EngineerID}')
        else:
            cursor.execute(
                "UPDATE Engineers SET FirstName=%s, LastName=%s, Rate=%s WHERE EngineerID=%s",
                (self.FirstName, self.LastName, self.Rate, self.EngineerID)
            )
            db.commit()
            print(
                f'Engineer "{self.FirstName} {self.LastName}" updated. ID: {self.EngineerID}')

    def delete(self) -> None:
        '''Delete the engineer from the database.'''
        cursor.execute("DELETE FROM Engineers WHERE EngineerID=%s",
                       (self.EngineerID,))
        db.commit()
        print(f'Engineer {self.FirstName} {self.LastName} deleted')


def getallengineers() -> list[Engineer]:
    '''Get all engineers from the database.'''
    cursor.execute("SELECT * FROM Engineers")
    return [Engineer(*engineer) for engineer in cursor.fetchall()]


def getengineerbyid(engineerid: int) -> Engineer:
    '''Get an engineer from the database.'''
    cursor.execute(
        "SELECT * FROM Engineers WHERE EngineerID=%s", (engineerid,))
    return Engineer(*cursor.fetchone())
