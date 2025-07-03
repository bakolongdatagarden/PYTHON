def number_types_demo():
    """
    INTEGERS

    Integers are numbers without a fractional part
        - They can be positive or negative
           - e.g., 1, -2, 0, 1000
    """
    # Set variable x to an integer,
    # and verify the data type with the type() function.
    print("\nNumber Types Demo:")
    print("\nInteger:")
    x = 9
    print(x)  
    print(type(x))  

    """
    FLOATS 

    Floats are numbers with fractional parts
        - They can also be positive or negative
        - They can have many numbers after the decimal point
            - e.g., 1.0, -2.5, 0.3333, 1000.123456789
    """
    # Set variable y to a float,
    print("\nFloat:")
    y = 19.5456
    print(y)
    print(type(y))

    # We can also specify a float with a fraction 
    print("\nFractional Float (22/7):")
    almost_pi = 22 / 7
    print(almost_pi)
    print(type(almost_pi))

    """
    One function that is particularuly useful for fractions is the round() function.
    It rounds a number to a specified number of decimal places.
    """
    # Round the float to 2 decimal places
    print("\nRounded Float (2 decimal places):")
    rounded_almost_pi = round(almost_pi, 2)
    print(rounded_almost_pi)
    print(type(rounded_almost_pi))

def booleans_demo():
    """
    BOOLEANS

    Booleans represent one of two values: True or False.
    """
    print("\nBooleans Demo:")
    print("\nTrue Boolean:")
    # Set variable is_gambian to True
    is_gambian = True
    print(is_gambian)
    print(type(is_gambian))

    # Set variable is_chinese to False
    print("\nFalse Boolean:")
    is_chinese = False
    print(is_chinese)
    print(type(is_chinese))


    # Booleans represeent the truth value of an expression.
    print("\nTrue Boolean Expression:")
    z_three = (1 < 2)
    print(z_three)
    print(type(z_three))

    print("\nFalse Boolean Expression:")
    z_four = (9 < 3)
    print(z_four)
    print(type(z_four))
 
    # The not operator negates a boolean value.
    # True becomes False, and False becomes True.
    print("\nNegated Boolean:")
    ceo_45 = not is_gambian
    print(ceo_45)
    print(type(ceo_45))

def strings_demo():
    """
    STRINGS

    Strings are a collection of characters
        - i.e., letters, numbers, symbols, and spaces
    """

    # Strings are commonly used to represent text
    print("\nStrings Demo:")
    print("\nBasic Text String:")
    opening = "Nyambi!"
    print(opening)

    """
    You can get the length of a string using the len() function.
    - e.g., len("Hello") returns 5
    """
    print("\nLength of String:")
    print(len(opening))  # Length of the string 'Nyambi!'

    """
    A special type of string is the empty string.
    - It has no characters and is represented by two quotes with nothing in between.
    """
    print("\nEmpty String:")
    empty_string = ""
    print(type(empty_string))  # Type of the empty string
    print(len(empty_string))  # Length of the empty string

    """
    If you put a number in quotation marks, it has a string data type.
    """
    print("\nString with Number:")
    spirit_number = "999"
    print(spirit_number)  
    print(type(spirit_number)) 

    """
    If we have a string that is convertible to a float, we can use float() to convert it.
        - We can't convert for example "Hello" to a float
    """
    print("\nString Converted to Float:")
    spirit_number_float = float(spirit_number)
    print(spirit_number_float)
    print(type(spirit_number_float))  # Type of the converted float

    """
    You can add two strings together just like you can add two numbers.
        - This is called string concatenation.
        - A longer string can be created by adding strings together.
    """
    print("\nString Concatenation:")
    full_name = "Nyambi" + " " + "Bakolong"
    print(full_name)  # Concatenated string
    print(type(full_name))  # Type of the concatenated string

    """
    It's not possible to do subtraction or division with strings.
    - You also can't multiply two strings together.
    - But you can multiple a string by an integer.
        - You can't do this with floats.

    This results in the string being repeated that many times.
    """
    print("\nString Multiplication:")
    motto = "Nyambi!" * 3
    print(motto)  
    print(type(motto))  

    

if __name__ == "__main__":
    # Change the function below to run the demo you want:
    # number_types_demo()
    # booleans_demo()
    strings_demo()