import math 

def boxes_needed(total_sq_meters, sq_meters_per_box):
    """Returns the number of boxes needed to cover the floor."""
    return math.ceil(total_sq_meters / sq_meters_per_box)

def get_positive_float(prompt):
    while True: 
        try: 
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number")
            else:
                return value 
        except ValueError:
            print("Invalid input. Please enter a number.")
            