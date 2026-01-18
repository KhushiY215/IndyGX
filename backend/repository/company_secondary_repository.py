from sqlmodel import select, Session
from ..database import get_session
from ..models import CompanySecondary

class CompanySecondaryRepository:

    @staticmethod
    def get(company_id: int):
        with get_session() as session:
            return session.get(CompanySecondary, company_id)

    @staticmethod
    def upsert(company_id: int, data: dict):
        with get_session() as session:
            obj = session.get(CompanySecondary, company_id)

            if not obj:
                obj = CompanySecondary(company_id=company_id, **data)
                session.add(obj)
            else:
                for key, value in data.items():
                    setattr(obj, key, value)

            session.commit()
            session.refresh(obj)
            return obj

    @staticmethod
    def delete(company_id: int):
        with get_session() as session:
            obj = session.get(CompanySecondary, company_id)
            if not obj:
                return False
            session.delete(obj)
            session.commit()
            return True
    @staticmethod
    def upsert(company_id: int, data: dict, session: Session):
        obj = session.get(CompanySecondary, company_id)

        if obj:
            for k, v in data.items():
                setattr(obj, k, v)
        else:
            obj = CompanySecondary(company_id=company_id, **data)
            session.add(obj)

        return obj
 