# Display alphabet in right triangle shape



for i in range(12):
    k = ord("A") + i
    for j in range(i + 1):
        print(chr(k), end=" ")
        k = k + 1
    print()
