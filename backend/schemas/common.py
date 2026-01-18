from pydantic import BaseModel
from typing import Generic, List, TypeVar

T = TypeVar("T")

class PaginationMeta(BaseModel):
    page: int
    page_size: int
    total_records: int
    total_pages: int

class PaginatedResponse(BaseModel, Generic[T]):
    data: List[T]
    meta: PaginationMeta
    

class BulkUpsertRequest(BaseModel):
    items: List[dict]
