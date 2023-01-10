from dataclasses import dataclass
from typing import Optional


@dataclass
class Studio:
    StudioID: Optional[int]
    AuthenticationID: int
    Name: str
    Rooms: list[int]
    Engineers: list[int]
    Assets: list[int]
    LogoURL: str
