q = '''* Advertising
* Aerospace & Defense
* Apparel Retail
* Apparel, Accessories & Luxury Goods
* Application Software
* Asset Management & Custody Banks
* Auto Parts & Equipment
* Biotechnology
* Building Products
* Casinos & Gaming
* Commodity Chemicals
* Communications Equipment
* Construction & Engineering
* Construction Machinery & Heavy Trucks
* Consumer Finance
* Data Processing & Outsourced Services
* Diversified Metals & Mining
* Diversified Support Services
* Electric Utilities
* Electrical Components & Equipment
* Electronic Equipment & Instruments
* Environmental & Facilities Services
* Gold
* Health Care Equipment
* Health Care Facilities
* Health Care Services
* Health Care Supplies
* Health Care Technology
* Homebuilding
* Hotels, Resorts & Cruise Lines
* Human Resource & Employment Services
* IT Consulting & Other Services
* Industrial Machinery
* Integrated Telecommunication Services
* Interactive Media & Services
* Internet & Direct Marketing Retail
* Internet Services & Infrastructure
* Investment Banking & Brokerage
* Leisure Products
* Life Sciences Tools & Services
* Movies & Entertainment
* Oil & Gas Equipment & Services
* Oil & Gas Exploration & Production
* Oil & Gas Refining & Marketing
* Oil & Gas Storage & Transportation
* Packaged Foods & Meats
* Personal Products
* Pharmaceuticals
* Property & Casualty Insurance
* Real Estate Operating Companies
* Regional Banks
* Research & Consulting Services
* Restaurants
* Semiconductors
* Specialty Chemicals
* Specialty Stores
* Steel
* Systems Software
* Technology Distributors
* Technology Hardware, Storage & Peripherals
* Thrifts & Mortgage Finance
* Trading Companies & Distributors'''

lines = q.split("\n")

print("[")
cnt = 1
for line in lines:
    line = line.replace('* ','')
    print('(\''+str(cnt)+'\''+',\''+line+'\'),')
    cnt+=1
print("]")
