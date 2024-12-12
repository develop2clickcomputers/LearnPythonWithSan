
removeagreement = ["GA_CIBC_MLI_REPO","GA_CIBC_MLI_SLA","GA_RBC_MLI_SLA","GA_JPM_JHLH_REPO","GA_JPM_JHNY_REPO","GA_BOA-ML_JHUSA_REPO","GA_JPM_JHUSA_REPO"]

with open('C:/Users/andavsa/agreements.txt', 'r') as file:
    agreementdetails = [line.strip() for line in file.readlines()]

print(f"Size of agreementdetails: {len(agreementdetails)}")

class UniqueArray:
    def __init__(self):
        self.elements = set()

    def add(self, value):
        if value not in self.elements:
            self.elements.add(value)
            return True
        return False

    def get_elements(self):
        return list(self.elements)
#searchString ="identifier ="
searchString ="bp.identifier="
equalSearch ="="
unique_array = UniqueArray()
for eachlines in agreementdetails:
    if searchString in eachlines:
        splitlines = eachlines.split("'", 4) # 3,4 single quotes '
        #print(f"{splitlines}")
        filtered_strings = [s for s in splitlines if equalSearch not in s] # splitlines arrays filters out equalsearch
        #print(f"{filtered_strings[1]}")
        #for filtered_string in filtered_strings:
        unique_array.add("'"+filtered_strings[1]+"'")

# Convert the list to a string with a delimiter (e.g., comma and space)
string = ", ".join(unique_array.get_elements())
print(f"{string}")