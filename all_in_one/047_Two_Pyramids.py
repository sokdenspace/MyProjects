# print two pyramids of stars

# print pyramid one
rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print(" ")

# new line between pattern one and two
print(" ")

# print pyramid two
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print(" ")
