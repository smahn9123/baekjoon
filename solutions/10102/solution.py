n = int(input(""))
vote = input("")
a, b = vote.count("A"), vote.count("B")
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")
