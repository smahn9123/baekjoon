import sys

lines = sys.stdin.readlines()
for line in lines:
    numbers = list(map(int, line.split()))
    ans = []
    for index, num in enumerate(numbers):
        a = numbers[index - 1] if index > 0 else 1
        b = num
        c = numbers[index + 1] if index < len(numbers) - 1 else 1
        ans.append(str(a * b * c))
    sys.stdout.write(" ".join(ans) + "\n")
