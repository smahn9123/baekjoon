import sys

lines = sys.stdin.readlines()
cards = set(lines[1].split())
questions = lines[3].split()

sys.stdout.write(" ".join(("1" if q in cards else "0" for q in questions)))
