def conditions_demo():
    """
    In programming, conditions are statements that are either True or False. 

    There are many different ways to write conditions in Python
        - some of the most common ways just compare two different values
    """

    # For example, let's check if 2 is greater than 3
    print("\nIs 2 greater than 3?")
    print(2 > 3)

    # We can also use conditions to compare the values of variables.

    var_one = 1 
    var_two = 2

    print("\nIs var_one less than 1?")
    print(var_one < 1)
    print("\nIs var_2 greater than or equal to var_one?")
    print(var_two >= var_one)

    """
    Here are some common comparison operators in Python:
    - Equal to: ==
    - Not equal to: !=
    - Greater than: >
    - Less than: <
    - Greater than or equal to: >=
    - Less than or equal to: <=

    Important Note: 
    When you check two values are equal, you must use two equal signs (==), not one (=).
    """

def conditional_statements_demo():
    """
    Conditional statements use conditions to modify how your function runs.

    They check the value of a condition, and if the condition evaluates to True, then a certain block of code is executed.

    Otherwise, if the condition is False, the code doesn't run. 
    """
    # IF STATEMENTS
    def if_statements():
        """
        The simplest type of conditional statement is an if statement. 

        We'll explore with our evaluate_temp() function below. The function accepts a body temperature (in Celsius) as input.
            - Initially, message is set to "Normal Temperature"
            - Then if temp > 38 is True (e.g., the body temperature is greater than 38C), the message is updated to "Fever!". 
            - Otherwise, if temp > 38 is False, then the message is not updated.
            - Finally, message is returned by the function.
        """

        def evaluate_temp(temp):
            # Set an initial message
            message = "Normal Temperature."
            # Update value of message only if temperature is greater than 38
            if temp > 38:
                message = "Fever!"
            return message
        print("\nWith 37C Temperature:")
        print(evaluate_temp(37))
        print("\nWith 39C temperature:")
        print(evaluate_temp(39))

    # IF...ELSE STATEMENTS
    def if_else_statements():
        """
        We can use "else" statements to run code if a statement is False. 

        The code under the "if" statement is run if the statement is True, and the code under "else" is run if the statement is false
        """
        def evaluate_temp_with_else(temp):
            if temp > 38:
                message = "Fever!"
            else: 
                message = "Normal Temperature"
            return message
        print("\nPatient has 30C temperature:")
        print(evaluate_temp_with_else(30))
        print("\nPatient has 40C temperature:")
        print(evaluate_temp_with_else(40))

    # IF...ELIF...ELSE STATEMENTS
    def if_elif_else_statements():
        """
        We can use "elif" (else if) to check if multiple conditions might be true. The function below:
            - First checks if temp > 38. If this is true, then the message is set to "Fever!".
            - As long as the message has not already been set, the function then checks if temp > 35. If this is true, then the message is set to "Normal temperature."
            - Then, if still no message has been set, the "else" statement ensures that the message is set to "Low temperature." message is printed.
        You can think of "elif" as saying..."okay, that previous condition (e.g, temp > 38) was false, so let's chekc if this new condition (e.g., temp > 35) might be true!
        """
        def evaluate_temp_with_elif(temp):
            if temp > 38:
                message = "Fever!"
            elif temp > 35:
                message = "Normal Temperature!"
            else: 
                message = "Low Temperature."
            return message 
        print("\nPatient has 42C temperature:")
        print(evaluate_temp_with_elif(42))
        print("\nPatient has 36C temperature:")
        print(evaluate_temp_with_elif(36))
        print("\nPatient has 34C temperature:")
        print(evaluate_temp_with_elif(34))

    def example_calculations():
        """
        We can also use conditional statements to perform different calculations.

        SCENARIO:

        You live in a country with only two tax brackts.
            - People earning less than $12,000 pays 25% in taxes.
            - Anyone earning $12,000 or more pays 30%. 
        """
        # Let's calculate how much tax is owed
        def get_taxes(earnings):
            if earnings < 12000:
                tax_owed = earnings * .25 # 25% tax
            else:
                tax_owed = earnings * .30 # 30% tax
            return tax_owed
        ana_taxes = get_taxes(9000)
        bob_taxes = get_taxes(15000)
        print(ana_taxes)
        print(bob_taxes)


    # Call subfunctions here
    # if_statements()
    # if_else_statements()
    # if_elif_else_statements()
    example_calculations()


if __name__ == "__main__":
#    conditions_demo()
   conditional_statements_demo()
