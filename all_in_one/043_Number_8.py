# display number 8 pattern in python

# outer loop
for row in range(7):
    # nested loop
    for col in range(5):
        # conditional statements
        if (col == 0 or col == 4) and (
            row == 1 or row == 5) or (
            row == 0 or row == 6) and (
            col > 0 and col < 4) or (
            row == 2 or row == 4) and (
            col == 1 or col == 3) or (
            row == 3 and col == 2):
            # display (#) symbol
            print("#", end="")
        else:
            print(end=" ")
    # new line after each row
    print("")
