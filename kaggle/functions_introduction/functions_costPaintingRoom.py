import math

"""
Imagine you're a home decorator, and you need to calculate the cost of painting a room.

Below, we define a function get_cost() that takes as input:

sqft_walls = total square feet of walls to be painted
sqft_ceiling = total square feet of ceiling to be painted
sqft_per_gallon = square feet that can be painted with one gallon of paint
cost_per_gallon = cost (in dollars) of one gallon of paint

The function will return the cost (in dollars) of putting one coat of paint on all walls and the ceiling.
"""

# Define the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = gallons_needed * cost_per_gallon
    return cost

"""
Now let's use the get_cost function to calculate the cost of applying one coat of paint to a room with: 
- 432 square feet of walls, and 
- 144 square feet of ceiling,

Assume that one gallon of paint covers 400 square feet and costs $15 per gallon. Also assuming we can buy partial gallons of paint.
"""

project_cost = get_cost(432, 144, 400, 15)
print(f"The cost of painting the room is: ${project_cost:.2f}")

"""
Now let's say we can no longer buy fractions of a gallon. 

For example, if we need 4.3 gallons, we must buy 5 gallons.

To handle this, we can modify the get_cost function to round up the number of gallons needed to the nearest whole number using the math.ceil() function.
 """

def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = math.ceil(total_sqft / sqft_per_gallon)  # Round up to the nearest whole gallon
    cost = gallons_needed * cost_per_gallon
    return cost