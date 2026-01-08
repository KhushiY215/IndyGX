from sqlmodel import select
from backend.database import get_session
from backend.models import (
    CompanyPrimary,
    CompanySecondary,
    CompetitiveIntelligence,
    ContactInformation,
    DigitalPresenceBrand,
    FinancialsFunding,
    IndygxAssessment,
    PartnershipsEcosystem,
)

class CompanyRepository:

    @staticmethod
    def list_companies():
        with get_session() as session:
            stmt = select(
                CompanyPrimary.company_id,
                CompanyPrimary.company_name
            )
            return session.exec(stmt).all()

    @staticmethod
    def get_company_by_id(company_id: str):  # ✅ TEXT ID
        with get_session() as session:
            stmt = (
                select(CompanyPrimary)
                .where(CompanyPrimary.company_id == company_id)
            )
            return session.exec(stmt).first()

    @staticmethod
    def get_company_full_profile(company_id: str):  # ✅ TEXT ID
        """
        Load full company aggregate using joins.
        """
        with get_session() as session:
            stmt = (
                select(CompanyPrimary)
                .where(CompanyPrimary.company_id == company_id)
            )
            company = session.exec(stmt).first()

            if not company:
                return None

            # Force-load relationships (lazy load)
            _ = company.secondary
            _ = company.competitive_intelligence
            _ = company.contact_information
            _ = company.digital_presence_brand
            _ = company.financials_funding
            _ = company.indygx_assessment
            _ = company.partnerships_ecosystem

            return company
