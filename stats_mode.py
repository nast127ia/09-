from typing import Optional
from pydantic import BaseModel

class Stats(BaseModel):
    base: str
    quote: str
    volume_24h: float
    last_trade_price: float
    bid: float
    ask: float
    high: float
    low: float
    open: float
    change_24h: Optional[float] = None
