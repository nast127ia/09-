from datetime import datetime
from typing import List
from pydantic import BaseModel

class Candle(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

class HistoricalData(BaseModel):
    data: List[Candle]
