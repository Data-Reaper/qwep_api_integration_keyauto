# generated by datamodel-codegen:
#   filename:  temp.json
#   timestamp: 2024-05-30T12:39:42+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, RootModel


class ModelItem(BaseModel):
    article: str
    brand: str
    currency: str
    group: str
    avgprice: Optional[float] = None
    cnt: Optional[int] = None
    maxprice: Optional[float] = None
    minprice: Optional[float] = None
    status: Optional[str] = None
    vendor: Optional[str] = None


class Model(RootModel[List[ModelItem]]):
    pass
