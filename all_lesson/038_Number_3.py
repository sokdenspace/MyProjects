# display number 3 in python

# outer loop
for row in range(7):
    # nested loop
    for col in range(6):
        # conditional statements
        if(col == 0 and (
            row == 1 or row == 5)) or (
            col == 1 or col == 2 or col == 3) and (
            row == 0 or row == 6) or (
            col == 4 and (
            row == 0 or row == 3 or row == 6)) or (
            col == 5 and (
            row != 0 and row != 3 and row != 6)):
            # display (#) symbol
            print("#", end="")
        else:
            print(end=" ")
    # new line after each row
    print()
