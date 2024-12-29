# This code is complicated than the best solution on BOJ.

import sys

words = []
max_length = 0
for s in sys.stdin:
    stripped_s = s.rstrip()
    words.append(stripped_s)
    if len(stripped_s) > max_length:
        max_length = len(stripped_s)
words = [word.ljust(max_length) for word in words]

ans = ""
for j in range(max_length):
    for i in range(5):
        if words[i][j] != " ":
            ans += words[i][j]

sys.stdout.write(ans)
