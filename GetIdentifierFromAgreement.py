removeagreement = ["GA_CIBC_MLI_REPO","GA_CIBC_MLI_SLA","GA_RBC_MLI_SLA","GA_JPM_JHLH_REPO","GA_JPM_JHNY_REPO","GA_BOA-ML_JHUSA_REPO","GA_JPM_JHUSA_REPO"]

with open('C:/Users/andavsa/agreements.txt', 'r') as file:
    agreementdetails = [line.strip() for line in file.readlines()]

print(f"Size of agreementdetails: {len(agreementdetails)}")

searchString ="identifier ="
equalSearch ="="
for eachlines in agreementdetails:
    if searchString in eachlines:
        splitlines = eachlines.split("'", 2)
        filtered_strings = [s for s in splitlines if equalSearch not in s]
        for filtered_string in filtered_strings:
            print(f"'{filtered_string}',")

    # Convert the list to a string with a delimiter (e.g., comma and space)
    string = ", ".join(agreementdetails)

    # Print the resulting string
    print(string)

    # Define the input string
    input_string = """
    Insert into lcr_agreement(lender_collateralization_rule,agreement) values(
    (select lcr.id from lender_collateralization_rule lcr
    join lender_schedule ls on ls.id=lcr.lender_schedule
    join lcr_counterparty lcp on lcp.lender_collateralization_rule=lcr.id
    where lcp.business_partner =(select partner_b from agreement where identifier ='GA_BB_MLI') and ls.name = 'MLI_CD'),(select id from agreement where identifier='GA_BB_MLI'));
    Go
    Insert into lcr_agreement(lender_collateralization_rule,agreement) values(
    (select lcr.id from lender_collateralization_rule lcr
    join lender_schedule ls on ls.id=lcr.lender_schedule
    join lcr_counterparty lcp on lcp.lender_collateralization_rule=lcr.id
    where lcp.business_partner =(select partner_b from agreement where identifier ='GA_BMO_MLI_LEGACY') and ls.name = 'MLI_CD'),(select id from agreement where identifier='GA_BMO_MLI_LEGACY'));
    Go
    """
    # Split the input string by "Go" and strip any leading/trailing whitespace
    statements = [stmt.strip() for stmt in input_string.split("Go") if stmt.strip()]
    print(f"Size of statements: {len(statements)}")
    # Print the cleaned SQL statements
    for statement in statements:
        print(statement)
        print("Go")

