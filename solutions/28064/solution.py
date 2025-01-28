import sys


def check_connectable(a: str, b: str):
    for i in range(len(a) - 1, -1, -1):
        if b.startswith(a[i:]):
            return True
    for i in range(len(b) - 1, -1, -1):
        if a.startswith(b[i:]):
            return True
    return False


names = [name.rstrip() for name in sys.stdin.readlines()[1:]]
count = 0

for i in range(len(names) - 1):
    for j in range(i + 1, len(names)):
        if check_connectable(names[i], names[j]):
            count += 1

print(count)
