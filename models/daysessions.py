from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class DaySession:
    DaySessionID: Optional[int]
    StartTime: datetime
    EndTime: datetime
    Minutes: int