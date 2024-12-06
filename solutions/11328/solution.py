n = int(input(""))
possible = True
for i in range(n):
    a, b = input("").split(" ")
    c = list(a)
    for x in b:
        if x in c:
            c.remove(x)
        else:
            possible = False
    if c:
        possible = False
    print("Possible" if possible else "Impossible")
    possible = True
