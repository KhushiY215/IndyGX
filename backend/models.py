from sqlmodel import SQLModel, Field, Relationship

class CompanyPrimary(SQLModel, table=True):
    __tablename__ = "company_primary"

    company_id: int = Field(primary_key=True)
    type: str | None
    company_name: str | None
    year_of_incorporation: str | None
    industry_segment: str | None
    nature_of_company: str
    website_url: str | None
    linkedin_profile_url: str | None
    ceo_name: str | None
    ceo_linkedin_url: str | None
    employee_size: str | None
    services_offerings: str | None
    core_value_proposition: str | None
    focus_sectors_industries: str | None
    countries_operating_in: str | None
    geographic_coverage_india: str | None

    secondary: "CompanySecondary"  = Relationship(back_populates="company")
    competitive_intelligence: "CompetitiveIntelligence"  = Relationship(back_populates="company")
    contact_information: "ContactInformation" = Relationship(back_populates="company")
    digital_presence_brand: "DigitalPresenceBrand" = Relationship(back_populates="company")
    financials_funding: "FinancialsFunding"  = Relationship(back_populates="company")
    indygx_assessment: "IndygxAssessment" = Relationship(back_populates="company")
    partnerships_ecosystem: "PartnershipsEcosystem"  = Relationship(back_populates="company")




class CompanySecondary(SQLModel, table=True):
    __tablename__ = "company_secondary"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    twitter_handle: str | None
    facebook_page_url: str | None
    instagram_page_url: str | None
    key_business_leaders_name: str | None
    key_business_leaders_linkedin_url: str | None
    regulatory_licenses_certifications: str | None
    compliance_track_record: str | None
    legal_issues_controversies: str | None
    processing_time: str | None
    success_rate: str | None

    company: "CompanyPrimary" = Relationship(back_populates="secondary")




class CompetitiveIntelligence(SQLModel, table=True):
    __tablename__ = "competitive_intelligence"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    competitors: str | None
    unique_differentiators: str | None
    competitive_advantages: str | None
    weakness_gaps: str | None
    key_challenges_needs: str | None

    company: "CompanyPrimary" = Relationship(back_populates="competitive_intelligence")




class ContactInformation(SQLModel, table=True):
    __tablename__ = "contact_information"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    contact_email: str | None
    phone_number: str | None
    primary_contact_person_name: str | None
    primary_contact_person_title: str | None
    primary_contact_person_email: str | None
    primary_contact_person_phone_number: str | None
    decision_maker_accessibility: str | None

    company: "CompanyPrimary" = Relationship(back_populates="contact_information")




class DigitalPresenceBrand(SQLModel, table=True):
    __tablename__ = "digital_presence_brand"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    quality_of_website: str | None
    awards_recognition: str | None
    brand_sentiment_score: str | None
    news_about_company: str | None
    average_deal_size: str | None
    top_customers: str | None
    website_traffic_rank: str | None
    social_media_followers_combined: str | None
    glassdoor_rating: str | None
    indeed_rating: str | None
    google_reviews_rating: str | None

    company: "CompanyPrimary" = Relationship(back_populates="digital_presence_brand")




class FinancialsFunding(SQLModel, table=True):
    __tablename__ = "financials_funding"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    annual_revenues: str | None
    annual_profits: str | None
    company_valuation: str | None
    yoy_growth_rate: str | None
    profitability_status: str | None
    market_share: str | None
    key_investors_backers: str | None
    exit_history: str | None
    recent_funding_rounds: str | None
    total_capital_raised: str | None

    company: "CompanyPrimary" = Relationship(back_populates="financials_funding")




class IndygxAssessment(SQLModel, table=True):
    __tablename__ = "indygx_assessment"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    previous_interactions: str | None
    partnership_potential_rating: str | None
    collaboration_opportunity_score: str | None
    complementary_services_match_score: str | None

    company: "CompanyPrimary" = Relationship(back_populates="indygx_assessment")





class PartnershipsEcosystem(SQLModel, table=True):
    __tablename__ = "partnerships_ecosystem"

    company_id: int = Field(primary_key=True, foreign_key="company_primary.company_id")
    corporate_partnership_programs: str | None
    university_academic_partnerships: str | None
    industry_associations_memberships: str | None
    strategic_partnerships: str | None
    rnd_investment_percentage: str | None
    technology_partners: str | None

    company: "CompanyPrimary" = Relationship(back_populates="partnerships_ecosystem")
 