studs = {'zark' : 90 , 'zainab' : 98 , 'sidra' : 89 , 'faiza' : 96 , 'ilma' : 99 }
usrinp = input("Enter a student's name : ")
lowcs = usrinp.lower()

if lowcs in studs :
    print(f"{usrinp}'s Marks are {studs[lowcs]} out of 100. ")
else:
    print(f"{usrinp}'s Name is not in the list. ")
    