pennies = int(input("How many pennies do you have?"))
dollars = 0
quarters = 0
dimes = 0
nickels = 0


while pennies >= 5:
    if pennies >= 100:
        pennies -= 100
        dollars += 1
    elif pennies >= 25:
        pennies -= 25
        quarters += 1    
    elif pennies >= 10:
        pennies -= 10
        dimes += 1
    elif pennies >= 5:
        pennies -= 5
        nickels += 1
        
print(f"""
{pennies} pennies, {dollars} dollars, {quarters} quarters, {dimes} dimes,  {nickels} nickels""")