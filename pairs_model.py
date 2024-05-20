from typing import List
from pydantic import BaseModel

class Pair(BaseModel):
    id: str
    base: str
    quote: str
    display_name: str
    margin_enabled: bool

class Pairs(BaseModel):
    data: List[Pair]
