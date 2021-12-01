# display number 7 pattern in python

i = 7
# outer loop
for row in range(i):
    # nested loop
    for col in range(i):
        # conditional statements
        if (row == 0 and col < 4) or (
            col == 4) or (row == 3 and (
            col > 1 and col < 7)):
            # display (#) symbol
            print("#", end="")
        else:
            print(end=" ")
    # new line after each row
    print("")
