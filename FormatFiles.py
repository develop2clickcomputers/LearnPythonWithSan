codes = ["058F",	"058H"
]
with open('C:/Users/andavsa/portfolio.txt', 'r') as file:
    portfolios = [line.strip() for line in file.readlines()]

print(f"Size of portfolios: {len(portfolios)}")
with open('C:/Users/andavsa/format.txt', 'r') as file:
    lines = file.readlines()
print(f"Size of line: {len(lines)}")
with open('C:/Users/andavsa/format.txt', 'w') as file:
    for line in lines:
        for code in portfolios:
            file.write(line.strip() + "," + code+"\n")