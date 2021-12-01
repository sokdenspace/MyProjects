# display number 4 pattern in python

i = 7
# outer loop
for row in range(i):
    # nested loop
    for col in range(i):
        # conditional statements
        if (col == 4 or row == 4) or (
            col == 3 and row == 1) or (
            col == 2 and row == 2) or (
            col == 1 and row == 3) or (
            row == 4):
            # display (*) symbol
            print("*", end="")
        else:
            print(end=" ")
    # new line after each row
    print("")
