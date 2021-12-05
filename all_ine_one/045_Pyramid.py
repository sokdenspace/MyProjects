# print reverse pyramid pattern
# in python

rows = 5
k = 2 * rows - 2
# outer loop
for i in range(rows, -1, -1):
    # nested loop
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        # display (#) symbol
        print("#", end=" ")
    print("")
