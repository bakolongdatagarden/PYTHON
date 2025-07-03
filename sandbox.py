"""
This program adds three to a user's input.
"""

def add_three():
    number = int(input("What's your number?: "))
    return number + 3

"""
This program adds three to a user's input if:
    - the input is less than 10
And adds eight if:
    - the input is 10 or more
"""
def add_three_or_eight():
    number = int(input("What's your number?: "))
    if number < 10:
        return number + 3
    else: 
        return number + 8

if __name__ == "__main__":
    # print(add_three())
    print(add_three_or_eight())