"""
This program uses information like the number of of bedroom and bathrooms to predict the price of a house.

We create the function get_expected_cost() that has two arguments: 

1. beds - number of bedrooms
2. baths - number of bathrooms

It should return the expected cost of a house with that number of bedrooms and bathrooms. Assume that: 

- The expected cost for a house with 0 bedrooms and bathrooms is 80,000.
- Each bedroom adds 30,000 to the expected cost.
- Each bathroom adds 10,000 to the expected cost. 

For instance, 
- A house with 1 bedroom 1 bathroom has an expected cost 120,000
- A house with 2 bedrooms and 1 bathroom has an expected cost of 150,000
"""

def get_expected_cost(beds, baths):
    """Returns the expected cost of a house based on the number of bedrooms and bathrooms."""
    value = 80000 + ((30000 * beds) + (10000 * baths))
    return value 


"""
Now that we have the function, we can test it with four different options:

A house with : 

1. 2 bedrooms and 3 bathrooms
2. 3 bedrooms and 2 bathrooms
3. 3 bedrooms and 3 bathrooms
4. 3 bedrooms and 4 bathrooms
"""

option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)

print(option_one)
print(option_two)
print(option_three) 
print(option_four)