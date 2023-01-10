from dataclasses import dataclass
from typing import Optional


@dataclass
class Asset:
    AssetID: Optional[int]
    Name: str
