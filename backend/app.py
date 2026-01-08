from backend.repository.company_repository import CompanyRepository

if __name__ == "__main__":
    companies = CompanyRepository.list_companies()
    print("Companies:")
    for c in companies:
        print(c)

    print("\nFull company profile:")
    company = CompanyRepository.get_company_full_profile(company_id="1")
    print(company)
 