from pydantic import BaseModel
from typing import Optional
from .company_primary import CompanyPrimaryRead
from .company_secondary import CompanySecondaryBase
from .competitive_intelligence import CompetitiveIntelligenceBase
from .contact_information import ContactInformationBase
from .digital_presence_brand import DigitalPresenceBrandBase
from .financials_funding import FinancialsFundingBase
from .indygx_assessment import IndygxAssessmentBase
from .partnerships_ecosystem import PartnershipsEcosystemBase


from .company_primary import CompanyPrimaryCreateUpdate
from .company_secondary import CompanySecondaryCreateUpdate
from .competitive_intelligence import CompetitiveIntelligenceCreateUpdate
from .contact_information import ContactInformationCreateUpdate
from .digital_presence_brand import DigitalPresenceBrandCreateUpdate
from .financials_funding import FinancialsFundingCreateUpdate
from .indygx_assessment import IndygxAssessmentCreateUpdate
from .partnerships_ecosystem import PartnershipsEcosystemCreateUpdate

class CompanyListItem(BaseModel):
    company_id: int
    company_name: str


class CompanyFullProfile(CompanyPrimaryRead):
    secondary: CompanySecondaryBase | None
    competitive_intelligence: CompetitiveIntelligenceBase | None
    contact_information: ContactInformationBase | None
    digital_presence_brand: DigitalPresenceBrandBase | None
    financials_funding: FinancialsFundingBase | None
    indygx_assessment: IndygxAssessmentBase | None
    partnerships_ecosystem: PartnershipsEcosystemBase | None
 
class CompanyFullProfileUpsert(BaseModel):
    primary: CompanyPrimaryCreateUpdate
    secondary: Optional[CompanySecondaryCreateUpdate] = None
    competitive_intelligence: Optional[CompetitiveIntelligenceCreateUpdate] = None
    contact_information: Optional[ContactInformationCreateUpdate] = None
    digital_presence_brand: Optional[DigitalPresenceBrandCreateUpdate] = None
    financials_funding: Optional[FinancialsFundingCreateUpdate] = None
    indygx_assessment: Optional[IndygxAssessmentCreateUpdate] = None
    partnerships_ecosystem: Optional[PartnershipsEcosystemCreateUpdate] = None