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
