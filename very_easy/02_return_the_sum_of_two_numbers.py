# Question 02:

# Return the Sum of Two Numbers

# Create a function that takes two numbers as arguments and returns their sum.

# Examples

# addition(3, 2) ➞ 5
# addition(-3, -6) ➞ -9
# addition(7, 3) ➞ 10

# Notes

# Don't forget to return the result.
# If you get stuck on a challenge, find help in the Resources tab.
# If you're really stuck, unlock solutions in the Solutions tab.

# def addition(a, b):

# Solution:


# Method 1: Function definition (def)


def addition(a: int, b: int) -> int:
    return a + b


# Method 2: Lambda expression (lambda)

addition = lambda a, b: a + b

print(addition(3, 2))
print(addition(-3, -6))
print(addition(7, 3))
