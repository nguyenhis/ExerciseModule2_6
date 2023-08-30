import random

def cast():
    first, second, third = random.randint(0,9), random.randint(0,9), random.randint(0,9)
    return first, second, third

die1, die2, die3 = cast()
print(f"The 3-digit code: {die1} {die2} {die3}.")

def cast():
    first, second, third, fourth = random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)
    return first, second, third, fourth

die1, die2, die3, die4 = cast()
print(f"The 4-digit code: {die1} {die2} {die3} {die4}.")
