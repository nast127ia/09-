from typing import Optional
from pydantic import BaseModel, Field, validator

class Stats(BaseModel):
    base: str = Field(..., description="Base currency symbol")
    quote: str = Field(..., description="Quote currency symbol")
    volume_24h: float = Field(..., ge=0, description="24h trading volume")
    last_trade_price: float = Field(..., ge=0, description="Last trade price")
    bid: float = Field(..., ge=0, description="Highest bid price")
    ask: float = Field(..., ge=0, description="Lowest ask price")
    high: float = Field(..., ge=0, description="24h highest price")
    low: float = Field(..., ge=0, description="24h lowest price")
    open: float = Field(..., ge=0, description="Opening price")
    change_24h: Optional[float] = Field(None, ge=-1, le=1, description="24h price change percentage")

    @validator('base', 'quote')
    def validate_symbols(cls, value):
        if not value.isalpha():
            raise ValueError('Currency symbols must only contain letters')
        return value
