from sys import stdin, stdout

next(stdin)
l = stdin.read().split()
stdout.write(f"{min(l, key=int)} {max(l, key=int)}")
