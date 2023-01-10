from dataclasses import dataclass
from typing import Optional


@dataclass
class Room:
    RoomID: Optional[int]
    Name: str
    Assets: list[int]
    Rate: float
