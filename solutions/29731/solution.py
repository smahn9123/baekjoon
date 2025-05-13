import sys

s = {
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
}

for line in sys.stdin.readlines()[1:]:
    if line.strip() not in s:
        sys.stdout.write("Yes")
        break
else:
    sys.stdout.write("No")
