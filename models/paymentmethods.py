from dataclasses import dataclass
from typing import Optional


@dataclass
class PaymentMethod:
    PaymentMethodID: Optional[int]
