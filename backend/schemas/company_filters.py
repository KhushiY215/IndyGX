from pydantic import BaseModel

class CompanyPrimaryFilter(BaseModel):
    company_name: str | None = None
    industry_segment: str | None = None
    country: str | None = None
    employee_size: str | None = None
 