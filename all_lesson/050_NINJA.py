# print Ninja say 'NO' pattern using 'yes' text

# outer loop
for row in range(6):
    # nested loop
    for col in range(16):
        if (col == 0) or (
            col == 1 and row == 1) or (
            col == 2 and row == 2) or (
            col == 3 and row == 3) or (
            col == 4 and row == 4) or (
            row == 0 or row == 5) and (
            col > 6 and col < 8) or (
            col == 5 and (row > 0 and row < 5)) or (
            col == 8 or col == 15) and (
            row > 1 and row < 4) or (
            col == 9 or col == 14) and (
            row == 1 or row == 4) or (
            row == 0 or row == 5) and (
            col > 12 and col < 15):
            # display 'yes' text
            print("yes", end="")
        else:
            print(end=" ")
    # new line after each row
    print("")
