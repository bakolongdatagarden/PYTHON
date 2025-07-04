def question_1():
    def get_grade(score):
        """
        Convert a numerical score to a letter grade according to standard scale.

        Args: 
            score (int): A numerical grade between 0-100 inclusive

        Returns:
            str: The corresponding letter grade ("A", "B", "C", "D", or "F")

        Grade Scale:
            A : 90-100
            B : 80-89
            C : 70-79
            D : 60-69
            F : <60
        """
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60: 
            grade = "D"
        else: 
            grade = "F"
        return grade 

    print(f"Your grade: {get_grade(100)}")

def question_2():
    def cost_of_project(engraving, solid_gold):
        """
        Remix of the original ring engraving program to practice with conditionals.

        Calculates the cost of a ring project based on engraving text and material.

        Args:
            engraving (str): the text to be engraved on the ring.
            solid_gold (bool): True if the ring is solid gold, False otherwise.

        Returns: 
            int: the total cost of the project.
        """
        if solid_gold == True:
            cost = 100 + (10 * len(engraving))
        else:
            cost = 50 + (7 * len(engraving))
        return cost
    engraving = input("What would you like to engrave?:\n")
    solid_gold_input = input("Would you like solid gold? (yes / no:\n").strip().lower()
    # Convert user input to boolean
    if solid_gold_input == "yes":
        solid_gold_bool = True
    elif solid_gold_input == "no":
        solid_gold_bool = False
    else:
        print("Invalid input for solid gold. Defeaulting to no.")
        solid_gold_bool = False
    print(f"The total cost of your ring will be ${cost_of_project(engraving, solid_gold_bool):,.2f}.")

def question_3():
    def get_water_bill(num_gallons):
        """
        Calculate a customer's monthly water bill using tiered pricing.

        The water agency uses a 4-tier pricing structure where the rate per gallon increases as water usage increases, encouraging conservation.

            Args:
                num_gallons (int) :  The number of gallons of water that a customer used that month.

            Returns
                float: The customer's water bill in U.S. dollars.
        """
        thousands_of_gallons = num_gallons / 1000

        if num_gallons <= 8000:
            bill = 5 * thousands_of_gallons
        elif num_gallons <= 22000:
            bill = 6 * thousands_of_gallons
        elif num_gallons <= 30000:
            bill = 7 * thousands_of_gallons
        else:
            bill = 10 * thousands_of_gallons
        return bill
    print(get_water_bill(1000))

def question_4():
    def get_data_bill(gb):
        """
        Calculate monthly data bill with base rate and overage charges.

        $100/month for up to 15 GB, then $.10/MB ($100GB) for additional usage.
        
        Args: 
            gb (float): The number of GB that the customer used in a month.

        Returns:
            (float): The customer's total data services bill in dollars.
        """
        if gb <= 15:
            bill = 100
        else:
            bill = 100 + (gb - 15) * 100
        return bill
    print(f"Your bill total is ${get_data_bill(15.1):,.2f}.")


if __name__ == "__main__":
    # Run question exercises indepedently for practice
    # question_1()
    # question_2()
    # question_3()
    question_4()