# display number 5 pattern in python

# outer loop
for row in range(7):
    # nested loop
    for col in range(6):
        # conditional statements
        if (row == 0 and (col > 0 and col < 6)) or (
            row == 1 or row == 2) and (col == 0) or (
            row == 3 or row == 6) and (
            col > 0 and col < 5) or (
            row == 4 and col == 5) or (
            row == 5 and (col == 0 or col == 5)):
            # display (#) symbol
            print("#", end="")
        else:
            print(end=" ")
    # new line after each row
    print("")
