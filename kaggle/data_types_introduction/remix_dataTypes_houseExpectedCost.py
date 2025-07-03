"""
House Expected Cost Estimator (Remix)

This program calculates the expected cost of a house based on user input for bedrooms, bathrooms, and whether it has a basement. 

This version is a remix of previous implementation, now enhanced with boolean handling for the basement feature.
"""

def get_expected_cost(beds: float, baths: float, has_basement: bool) -> float:
    """
    Calculate the expected cost of a house based on bedrooms, bathrooms, and basement.

    Args: 
        beds (float): Number of bedrooms.
        baths (float): Number of bathrooms
        hase_basement (bool): Whether the house has a basement.

    Returns: 
        float: The expected cost of the house.
    """
    return 80000 + 30000 * beds + 10000 * baths + (40000 if has_basement else 0)

def get_bool_input(prompt: str) -> bool:
    """
    Prompt the user for a yes/no answer and return a boolean.

    Args: 
        prompt (str): The prompt to display.
    Returns: 
        bool: True is user enters 'yes', False if 'no'.
    """
    while True: 
        response = input(prompt).strip().lower()
        if response in ('yes', 'y'):
            return True
        elif response in ('no', 'n'):
            return False
        else:
            print("Please enter 'yes' or 'no'.")
def main():
    try:
        beds = float(input("Enter the number of bedrooms: "))
        baths = float(input("Enter the number of bathrooms: "))
        has_basement = get_bool_input("Does the house have a basement? (yes/no): ")
        cost = get_expected_cost(beds, baths, has_basement)
        print(f"the expected cost of the house with {beds:.0f} bedrooms, {baths:.0f} bathrooms, "
        f"{'with' if has_basement else 'without'} a basement is: ${cost:.0f}")
    except ValueError:
        print("Please enter valid numbers for the number of bedrooms and bathrooms.")

if __name__ == "__main__":
    main()