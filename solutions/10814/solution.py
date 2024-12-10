n = int(input())
people = []
for i in range(n):
    age, name = input().split(" ")
    people.append((int(age), name, i))

people_sorted = sorted(people, key=lambda x: (x[0], x[2]))
for i in people_sorted:
    print(i[0], i[1])
