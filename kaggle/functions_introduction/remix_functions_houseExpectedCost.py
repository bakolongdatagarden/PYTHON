"""
This program is a remix of the kaggle house expected cost program. It asks the user for the number of bedrooms and bathrooms in a house to predict its price.


We create the function get_expected_cost() that has two arguments: 

1. beds - number of bedrooms
2. baths - number of bathrooms

Then it prompts the user to input the number of bedrooms and bathrooms.

After that, it calls the get_expected_cost() function with the user inputs and prints the expected cost of the house.
"""

def get_expected_cost(beds, baths):
    """Returns the expected cost of a house based on the number of bedrooms and bathrooms."""
    value = 80000 + ((30000 * beds) + (10000 * baths))
    return value 

try:
    beds = int(input("Enter the number of bedrooms: "))
    baths = int(input("Enter the number of bathrooms: "))
    cost = get_expected_cost(beds, baths)
    print(f"The expected cost of the house with {beds} bedrooms and {baths} bathrooms is: ${cost:,}")
except ValueError:
    print("Please enter valid integers for the number of bedrooms and bathrooms.")