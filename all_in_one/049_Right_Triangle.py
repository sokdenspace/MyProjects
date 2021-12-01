# print right pascal's triangle
# pattern in python

rows = 5
# display triangle above
for i in range(0, rows):
    for j in range(0, i + 1):
        print("#", end=" ")
    print("\r")

# display triangle at the bottom
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("#", end=" ")
    print("\r")
