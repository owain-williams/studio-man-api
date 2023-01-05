from dataclasses import dataclass
from typing import Optional


@dataclass
class Engineer:
    EngineerID: Optional[int]
    FirstName: str
    LastName: str
    Rate: float
