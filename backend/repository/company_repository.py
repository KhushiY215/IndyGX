from typing import Any
from sqlmodel import select, func, Session

from backend.database import get_session
from backend.models import CompanyPrimary


class CompanyRepository:

    @staticmethod
    def list_companies(filters, page: int, page_size: int):
        page = max(page, 1)
        page_size = max(page_size, 1)

        with get_session() as session:
            query = select(CompanyPrimary)

            if filters.company_name:
                query = query.where(
                    CompanyPrimary.company_name.ilike(
                        f"%{filters.company_name}%"
                    )
                )

            if filters.industry_segment:
                query = query.where(
                    CompanyPrimary.industry_segment == filters.industry_segment
                )

            total = session.exec(
                select(func.count()).select_from(query.subquery())
            ).one()

            results = session.exec(
                query.offset((page - 1) * page_size)
                     .limit(page_size)
            ).all()

            return results, total

    @staticmethod
    def get_company_by_id(company_id: int):
        with get_session() as session:
            stmt = select(CompanyPrimary).where(
                CompanyPrimary.company_id == company_id
            )
            return session.exec(stmt).first()

    @staticmethod
    def get_company_full_profile(company_id: int):
        with get_session() as session:
            stmt = select(CompanyPrimary).where(
                CompanyPrimary.company_id == company_id
            )
            company = session.exec(stmt).first()

            if not company:
                return None

            # Lazy-load 1–1 relationships
            _ = company.secondary
            _ = company.competitive_intelligence
            _ = company.contact_information
            _ = company.digital_presence_brand
            _ = company.financials_funding
            _ = company.indygx_assessment
            _ = company.partnerships_ecosystem

            return company

    @staticmethod
    def upsert(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ) -> CompanyPrimary:
        data["company_id"] = company_id

        stmt = select(CompanyPrimary).where(
            CompanyPrimary.company_id == company_id
        )
        existing = session.exec(stmt).one_or_none()

        if existing:
            for k, v in data.items():
                setattr(existing, k, v)
            session.add(existing)
            return existing

        obj = CompanyPrimary(**data)
        session.add(obj)
        return obj
