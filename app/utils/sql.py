def get_sql_for_fetching_data(monthEnd=101):

    sql_string = '''
    -- LIST OF CLIENTS-LOANS
    select
    L.pkMonthEnd, pkLoanDeliquency, average_Overdue_days,
    -- CLIENT DATA
    (select clientCode from D_CLIENT WHERE pkClient = C.pkClient) as clientCode, 
    C.familyMembers as familyMembers, 
    (select clientAge from D_CLIENTAGE WHERE pkClientAge = C.pkClientAge) as clientAge, 
    (select gender from D_GENDER WHERE pkClientGender = C.pkClientGender) as clientGender, 
    (select maritalStatus from D_MARITALSTATUS WHERE pkMaritalStatus = C.pkMaritalStatus) as maritalStatus, 
    (select economicSector from D_ECONOMICSECTOR WHERE pkEconomicSector = C.pkEconomicSector) as economicSector, 
    (select education from D_EDUCATION WHERE pkClientEducation = C.pkClientEducation) as clientEducation, 
    (select idType from D_IDTYPE WHERE pkClientIdType = C.pkClientIdType) as clientIdType, 
    (select AddressDistrict from D_ADDRESSDISTRICT WHERE pkClientAddressDistrict = C.pkClientAddressDistrict) as clientAddressDistrict,
    -- CREDIT DATA
    (select amountbracket from D_AMOUNTBRACKET WHERE pkLoanAmountBracket = L.pkLoanAmountBracket) as LoanAmountBracket, 
    (select branch from D_BRANCH WHERE pkLoanBranch = L.pkLoanBranch) as LoanBranch, 
    (select CreditLineCode from D_CREDITLINE WHERE pkCreditLine = L.pkCreditLine) as CreditLine, 
    (select Currency from D_CURRENCY WHERE pkLoanCurrency = L.pkLoanCurrency) as Currency, 
    (select deliquency from D_DELIQUENCY WHERE pkLoanDeliquency = L.pkLoanDeliquency) as Deliquency, 
    (select InterestRate from D_INTEREST WHERE pkLoanInterestRate = L.pkLoanInterestRate) as InterestRate, 
    (select newRepeated from D_NEWREPEATED WHERE pkLoanNewRepeated = L.pkLoanNewRepeated) as LoanNewRepeated, 
    (select Product from D_PRODUCT WHERE pkLoanProduct = L.pkLoanProduct) as Product, 
    (select Purpose from D_PURPOSE WHERE pkLoanPurpose = L.pkLoanPurpose) as Purpose, 
    (select Status from D_STATUS WHERE pkLoanStatus = L.pkLoanStatus) as Status, 
    amount_Credit_Request,
    pkLoanCode as LoanCode
    from dbo.D_CLIENT C, F_CREDIT L where pkMonthEnd = {monthEnd} and C.pkClient = L.pkClient
    order by clientCode
    '''.format(monthEnd = monthEnd)

    return sql_string
