removeagreement = ["GA_CIBC_MLI_REPO","GA_CIBC_MLI_SLA","GA_RBC_MLI_SLA","GA_JPM_JHLH_REPO","GA_JPM_JHNY_REPO","GA_BOA-ML_JHUSA_REPO","GA_JPM_JHUSA_REPO"]
#removeagreement = ["GA_BB_MLI"]

with open('C:/Users/andavsa/agreements.txt', 'r') as file:
    agreementdetails = [line.strip() for line in file.readlines()]

print(f"Size of agreementdetails: {len(agreementdetails)}")

searchString ="identifier ="
equalSearch ="="
# Convert the list to a string with a delimiter (e.g., comma and space)
input_string = "\n".join(agreementdetails)
# Print the resulting string
#print(input_string)
# Split the input string by "Go" and strip any leading/trailing whitespace
statements = [stmt.strip() for stmt in input_string.split("Go") if stmt.strip()]
print(f"Size of statements: {len(statements)}")
# Print the cleaned SQL statements
with open('C:/Users/andavsa/agreementsupdated.txt', 'w') as fileupdated:
    for statement in statements:
        if not any(element in statement for element in removeagreement):
        #for element in removeagreement:
            #if element not in statement:
                fileupdated.write(statement)
                fileupdated.write("\n")
                fileupdated.write("Go")
                fileupdated.write("\n")

                #print({len(statement)})
                #print(statement)
                #print("Go")


