def get_sql_for_fetching_data(monthEnd=101):

    sql_string = '''
    -- LIST OF CLIENTS-LOANS
    select
    L.pkMonthEnd,
    -- CLIENT DATA
    (select clientCode from D_CLIENT WHERE pkClient = C.pkClient) as clientCode, 
    C.familyMembers, 
    (select clientAge from D_CLIENTAGE WHERE pkClientAge = C.pkClientAge) as clientAge, 
    (select gender from D_GENDER WHERE pkClientGender = C.pkClientGender) as gender, 
    (select maritalStatus from D_MARITALSTATUS WHERE pkMaritalStatus = C.pkMaritalStatus) as maritalStatus, 
    (select economicSector from D_ECONOMICSECTOR WHERE pkEconomicSector = C.pkEconomicSector) as economicSector, 
    (select education from D_EDUCATION WHERE pkClientEducation = C.pkClientEducation) as education, 
    (select idType from D_IDTYPE WHERE pkClientIdType = C.pkClientIdType) as idType,
    (select AddressDistrict from D_ADDRESSDISTRICT WHERE pkClientAddressDistrict = C.pkClientAddressDistrict) as AddressDistrict,
    -- CREDIT DATA
    (select amountbracket from D_AMOUNTBRACKET WHERE pkLoanAmountBracket = L.pkLoanAmountBracket) as amountbracket, 
    (select branch from D_BRANCH WHERE pkLoanBranch = L.pkLoanBranch) as branch, 
    (select CreditLineCode from D_CREDITLINE WHERE pkCreditLine = L.pkCreditLine) as CreditLineCode, 
    (select Currency from D_CURRENCY WHERE pkLoanCurrency = L.pkLoanCurrency) as Currency,
    (select deliquency from D_DELIQUENCY WHERE pkLoanDeliquency = L.pkLoanDeliquency) as deliquency, 
    (select InterestRate from D_INTEREST WHERE pkLoanInterestRate = L.pkLoanInterestRate) as InterestRate, 
    (select newRepeated from D_NEWREPEATED WHERE pkLoanNewRepeated = L.pkLoanNewRepeated) as newRepeated, 
    (select Product from D_PRODUCT WHERE pkLoanProduct = L.pkLoanProduct) as Product, 
    (select Purpose from D_PURPOSE WHERE pkLoanPurpose = L.pkLoanPurpose) as Purpose, 
    (select Status from D_STATUS WHERE pkLoanStatus = L.pkLoanStatus) as Status, 
    amount_Credit_Request,
    pkLoanCode
    from dbo.D_CLIENT C, F_CREDIT L where pkMonthEnd = {monthEnd} and C.pkClient = L.pkClient
    order by clientCode
    '''.format(monthEnd = monthEnd)

    return sql_string


def get_sql_for_bad_loans(num_rows=10000):

    sql_string = '''
    -- LIST OF CLIENTS-LOANS
    select
    top {}
    L.pkMonthEnd,
    -- CLIENT DATA
    (select clientCode from D_CLIENT WHERE pkClient = C.pkClient) as clientCode, 
    C.familyMembers, 
    (select clientAge from D_CLIENTAGE WHERE pkClientAge = C.pkClientAge) as clientAge, 
    (select gender from D_GENDER WHERE pkClientGender = C.pkClientGender) as gender, 
    (select maritalStatus from D_MARITALSTATUS WHERE pkMaritalStatus = C.pkMaritalStatus) as maritalStatus, 
    (select economicSector from D_ECONOMICSECTOR WHERE pkEconomicSector = C.pkEconomicSector) as economicSector, 
    (select education from D_EDUCATION WHERE pkClientEducation = C.pkClientEducation) as education, 
    (select idType from D_IDTYPE WHERE pkClientIdType = C.pkClientIdType) as idType,
    (select AddressDistrict from D_ADDRESSDISTRICT WHERE pkClientAddressDistrict = C.pkClientAddressDistrict) as AddressDistrict,
    -- CREDIT DATA
    (select amountbracket from D_AMOUNTBRACKET WHERE pkLoanAmountBracket = L.pkLoanAmountBracket) as amountbracket, 
    (select branch from D_BRANCH WHERE pkLoanBranch = L.pkLoanBranch) as branch, 
    (select CreditLineCode from D_CREDITLINE WHERE pkCreditLine = L.pkCreditLine) as CreditLineCode, 
    (select Currency from D_CURRENCY WHERE pkLoanCurrency = L.pkLoanCurrency) as Currency, 
    (select deliquency from D_DELIQUENCY WHERE pkLoanDeliquency = L.pkLoanDeliquency) as deliquency, 
    (select InterestRate from D_INTEREST WHERE pkLoanInterestRate = L.pkLoanInterestRate) as InterestRate, 
    (select newRepeated from D_NEWREPEATED WHERE pkLoanNewRepeated = L.pkLoanNewRepeated) as newRepeated, 
    (select Product from D_PRODUCT WHERE pkLoanProduct = L.pkLoanProduct) as Product, 
    (select Purpose from D_PURPOSE WHERE pkLoanPurpose = L.pkLoanPurpose) as Purpose, 
    (select Status from D_STATUS WHERE pkLoanStatus = L.pkLoanStatus) as Status, 
    amount_Credit_Request,
    pkLoanCode
    from dbo.D_CLIENT C, F_CREDIT L 
    where pkLoanDeliquency > 3 and C.pkClient = L.pkClient
    order by clientCode
    '''.format(num_rows)

    return sql_string

def get_sql_for_good_loans(num_rows=10000):

    sql_string = '''
    -- LIST OF CLIENTS-LOANS
    select
    top {}
    L.pkMonthEnd,
    -- CLIENT DATA
    (select clientCode from D_CLIENT WHERE pkClient = C.pkClient) as clientCode, 
    C.familyMembers, 
    (select clientAge from D_CLIENTAGE WHERE pkClientAge = C.pkClientAge) as clientAge, 
    (select gender from D_GENDER WHERE pkClientGender = C.pkClientGender) as gender, 
    (select maritalStatus from D_MARITALSTATUS WHERE pkMaritalStatus = C.pkMaritalStatus) as maritalStatus, 
    (select economicSector from D_ECONOMICSECTOR WHERE pkEconomicSector = C.pkEconomicSector) as economicSector, 
    (select education from D_EDUCATION WHERE pkClientEducation = C.pkClientEducation) as education, 
    (select idType from D_IDTYPE WHERE pkClientIdType = C.pkClientIdType) as idType,
    (select AddressDistrict from D_ADDRESSDISTRICT WHERE pkClientAddressDistrict = C.pkClientAddressDistrict) as AddressDistrict,
    -- CREDIT DATA
    (select amountbracket from D_AMOUNTBRACKET WHERE pkLoanAmountBracket = L.pkLoanAmountBracket) as amountbracket, 
    (select branch from D_BRANCH WHERE pkLoanBranch = L.pkLoanBranch) as branch, 
    (select CreditLineCode from D_CREDITLINE WHERE pkCreditLine = L.pkCreditLine) as CreditLineCode, 
    (select Currency from D_CURRENCY WHERE pkLoanCurrency = L.pkLoanCurrency) as Currency, 
    (select deliquency from D_DELIQUENCY WHERE pkLoanDeliquency = L.pkLoanDeliquency) as deliquency, 
    (select InterestRate from D_INTEREST WHERE pkLoanInterestRate = L.pkLoanInterestRate) as InterestRate, 
    (select newRepeated from D_NEWREPEATED WHERE pkLoanNewRepeated = L.pkLoanNewRepeated) as newRepeated, 
    (select Product from D_PRODUCT WHERE pkLoanProduct = L.pkLoanProduct) as Product, 
    (select Purpose from D_PURPOSE WHERE pkLoanPurpose = L.pkLoanPurpose) as Purpose, 
    (select Status from D_STATUS WHERE pkLoanStatus = L.pkLoanStatus) as Status, 
    amount_Credit_Request,
    pkLoanCode
    from dbo.D_CLIENT C, F_CREDIT L 
    where pkLoanDeliquency <= 3 and C.pkClient = L.pkClient
    order by clientCode
    '''.format(num_rows)

    return sql_string
