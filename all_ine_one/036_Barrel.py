# Display barrel shape in Python

for row in range(7):
    for col in range(10):
        if(row == 0 or row == 6) and (
            col > 1 and col < 8) or (
            row == 1 or row == 5) and (
            col < 2 and col > 0 or col == 8) or (
            row == 2 or row == 3 or row == 4) and (
            col == 0 or col == 9):
            print("*", end="")
        else:
            print(end=" ")
    print()
