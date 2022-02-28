# Display number 1 shape in Python

for row in range(5):
    for col in range(9):
        if (row == 1 and col < 5) and (
            col > 1 and col != 3) or (
            row == 4 or col == 4) or (
            row == 2 and col == 0 and col < 4):
            print("*", end="")
        else:
            print(end=" ")
    print()
