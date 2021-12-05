'''-------->challenge<--------
equation: 2x^2 - 11x + 14 = 0
1. find discriminant of equation?
2. find root1 and root2 of equation?'''

import math
# declare the variable to store
# value in-memory temporary
a = int(2); b = int(-11); c = int(14)

# 1. find discriminant of equation
discriminant = pow(b, 2) - (4 * a * c)

# 2. find root1 and root2 of equation
root1 = (-b - math.sqrt(discriminant)) / (2 * a)
root2 = (-b + math.sqrt(discriminant)) / (2 * a)

# print output the results
print("\n===answer===")
print("root1 = ", root1)
print("root2 = ", root2)
print("\n")
