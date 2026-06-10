# Question 03

# Return the Next Number from the Integer Passed

# Create a function that takes a number as an argument, increments the number by +1 and returns the result.

# Examples

# addition(0) ➞ 1
# addition(9) ➞ 10
# addition(-3) ➞ -2

# Notes

# Don't forget to return the result.
# If you get stuck on a challenge, find help in the Resources tab.
# If you're really stuck, unlock solutions in the Solutions tab.

# Code

# def addition(num):


# Solution

# Method 1: Function definition (def)


def addition(num: int) -> int:
    return num + 1


# Method 2: Lambda expression (lambda)

addition = lambda num: num + 1

# Verification

print(addition(0))
print(addition(9))
print(addition(-3))
