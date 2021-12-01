# display number 6 pattern in python

# outer loop
for row in range(7):
    # nested loop
    for col in range(6):
        # conditional statements
        if (row == 3 and col < 4) or (
            col == 0 or col == 4) and (
            row > 3 and row < 6) or (
            col == 0 and (row < 3 and row > 0)) or (
            row == 0 and (col > 0 and col < 5)) or (
            row == 6 and (col > 0 and col < 4)):
            # display (#) symbol
            print("#", end="")
        else:
            print(end=" ")
    # new line after each row
    print("")
