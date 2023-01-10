from dataclasses import dataclass
from typing import Optional
from db import db
import json

cursor = db.cursor()


@dataclass
class Client:
    ClientID: Optional[int]
    ContactFirstName: str
    ContactLastName: str
    PaymentMethods: list[int] = None

    def commit(self) -> None:
        '''Add or update the client in the database.'''
        if self.ClientID is None:
            cursor.execute(
                "INSERT INTO Clients (ContactFirstName, ContactLastName) VALUES (%s, %s)",
                (self.ContactFirstName, self.ContactLastName)
            )
            self.ClientID = cursor.lastrowid
            print(
                f'Client "{self.ContactFirstName} {self.ContactLastName}" created. ID: {self.ClientID}')
        else:
            cursor.execute(
                "UPDATE Clients SET ContactFirstName=%s, ContactLastName=%s WHERE ClientID=%s",
                (self.ContactFirstName, self.ContactLastName, self.ClientID)
            )
            print(
                f'Client "{self.ContactFirstName} {self.ContactLastName}" updated. ID: {self.ClientID}')

    def delete(self) -> None:
        '''Delete the client from the database.'''
        cursor.execute("DELETE FROM Clients WHERE ClientID=%s",
                       (self.ClientID,))
        print(f'Client {self.ContactFirstName} {self.ContactLastName} deleted')

    def toJSON(self):
            return json.dumps(self, default=lambda o: o.__dict__, 
                sort_keys=True, indent=4)

def getallclients() -> list[Client]:
    '''Get all clients from the database.'''
    cursor.execute("SELECT * FROM Clients")
    allclients = cursor.fetchall()
    for client in allclients:
        client = client.toJSON()
    return allclients


def getoneclient(clientid: int) -> Client:
    '''Get a client from the database.'''
    cursor.execute("SELECT * FROM Clients WHERE ClientID=%s", (clientid,))
    return Client(*cursor.fetchone())


def getclientsbylastname(lastname: str) -> list[Client]:
    '''Get clients from the database by last name.'''
    cursor.execute(
        "SELECT * FROM Clients WHERE ContactLastName=%s", (lastname,))
    return [Client(*client) for client in cursor.fetchall()]
