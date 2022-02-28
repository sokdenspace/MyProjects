# Display (+) using % symbol in Python

for row in range(11):
    for col in range(11):
        if(row == 5 or col == 10):
            print("%", end=" ")
        else:
            print(end=" ")
    print()
