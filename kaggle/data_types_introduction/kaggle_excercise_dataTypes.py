
def question_1():
    """
    Below we practice how to convert a float to an integer using the int() function.
    """
    print("\nQuestion 1: Part 1")
    # Define a float
    y = 1.
    print(y)
    print(type(y))

    # Convert float to integer with the int function
    z = int(y)
    print(z)
    print(type(z))


    """
    The float we used has no numbers after the decimal point.
        - But what happens if we try to convert a float with a fractional part to an integer?
        - How does the outcome of the int function change for positive and negative numbers?

    Let's experiment with this.
    """
    print("\nQuestion 1: Part 2")
    print(int(1.2321)) # prints 1
    print(int(1.747)) # prints 1
    print(int(-3.94535)) # prints -3
    print(int(-2.19774)) # prints -2

    """
    EXPLANATION:
        In the example above,  we see that using the int() function:
            - Negative floats are always rounded UP to the closest integer
        - Positive floats are always rounded DOWN to the closest integer
    """

def question_2():
    """
    In the tutorial, we learned about booleans (which can be True or False).
        - We also learned about integers, floats, and strings.
    
    For this question, our goal is to find out what happens when we multiply a boolean by any of these data types. Specifically,

        - What happens when we multiply an integer or float by True? What happens when we multiply by False? How does the answer change if the numbers are positive or negative?
        - What happens when we multiply a string by True? By False?

    Let's investigate this.
    """
    print("\nQuestion 2")
    print(3 * True)
    print(-3.1 * True)
    print(type("abc * False"))
    print("abc" * True)
    print("abc" * False)
    print(len("abc" * False))

    """
    EXPLANATION:
        - Multiplying an integer or float by a boolean value True returns the same integer or float.
            - You're basically multiplying the number by 1.
            - Multiplying an integer or float by a boolean value False returns 0. 
            - This is true for both positive and negative numbers.
        - Multiplying a string by True returns the string itself.
            - And if you multiply a string by False, it returns an empty string.
            - The length of the empty string is 0.
    """
def question_3():
    """
    In this question, we will build off our work from a previous exercise where we created a function to calculate the expected cost of a house based on the number of bedrooms and bathrooms.

    We create a function get_expected_cost() that takes 3 variables as input:
        - beds: number of bedrooms (data type float)
        - baths: number of bathrooms (data type float)
        - has_basement: whether the house has a basement (data type boolean)

    It should return the expected cost of a house with that number of bedrooms and bathrooms, and whether it has a basement. Assume that:
        - The expected cost for a house with 0 bedrooms and bathrooms is 80,000.
        - Each bedroom adds 30,000 to the expected cost.
        - Each bathroom adds 10,000 to the expected cost.
        - A basement adds 40,000 to the expected cost.

    For instance,
    - A house with 1 bedroom, 1 bathroom, and no basement has an expected cost of 120,000.
        - (80000 + 30000 + 10000 + 0 = 120000)
        - This value is calculated as follows:
            get_expected_cost(1, 1, False)
    - A house with 2 bedrooms, 1 bathroom, and a basement has an expected cost of 190,000
        - (80000 + 2 * 30000 + 10000 + 40000 = 190000)
        - This value is calculated as follows:
            get_expected_cost(2, 1, True)
    """
    def get_expected_cost(beds, baths, has_basement):
        """
        Returns the expected cost of a house based on the number of bedrooms, bathrooms, and whether it has a basement.
        """
        value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
        return value

def question_4():
    """
    We continue our study of boolean arithmetic. 

    What happens when you add booleans? 
    """
    print("\nQuestion 4: Adding Booleans")
    print(False + False)
    print(True + False)
    print(False + True)
    print(True + True)
    print(False + True + True + True)

    """
    EXPLANATION:

    When you add booleans,
     - adding False is equivalent to adding 0,
     - and adding True is equivalent to adding 1.

    """

def question_5():
    """
    SCENARIO:

    You own an online shop where you sell rings with custom engravings. 
    
    You offer both gold plated and solid gold rings.
        - Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
        - Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
        - Spaces and punctuation are counted as engraved units
    Write a function cost_of_project() that takes two arguments:
        - engraving: a Python string with the text of engraving
        - solid_gold: a Boolean that indicates whether the ring is solid gold 

    It should return the cost of the project
    """
def cost_of_project(engraving, solid_gold):
    if solid_gold:
        base_cost = 100
        per_character_rate = 10
    else: 
        base_cost = 50
        per_character_rate = 7
    total_cost = base_cost + per_character_rate * len(engraving)
    return total_cost

project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

project_two = cost_of_project("08/101/2000", False)
print(project_two)

project_three = cost_of_project("Nyambi", True)
print(project_three)

"""
# Kaggle's version of the solution
def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost 
"""

if __name__ == "__main__":
    # Change the function below to run the demo you want:
    # question_1()
    # question_2()
    # question_3()
    # question_4()
    question_5()