"""
This program calculates how much taxes someone owes based on their income.

    If they earn less than $12,000, they are taxed 25% of their income.

    If they earn $12,000 or more, they are taxes 30% of their income.
"""       
def get_taxes(): # empty argument because ... 
        while True:
            try: 
                earnings = float(input("Enter your earnings: $"))
                if earnings < 12000:
                    tax_owed = earnings * .25
                else: 
                    tax_owed = earnings * .30 
                return tax_owed 
            except ValueError: 
                print("Invalid input. Please enter a number.")
print(f"You owe ${get_taxes():,.2f} in taxes")
 