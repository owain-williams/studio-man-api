from dataclasses import dataclass
from typing import Optional
from db import cursor


@dataclass
class Engineer:
    EngineerID: Optional[int]
    FirstName: str
    LastName: str
    Rate: float

    def setrate(self, rate: float) -> None:
        '''Set the engineer's rate.'''
        db.execute("UPDATE Engineers SET Rate=%s WHERE EngineerID=%s",
                   (rate, self.EngineerID))
        db.commit()
        self.Rate = rate
        print(f'Engineer {self.FirstName} {self.LastName} rate set to {rate}')
