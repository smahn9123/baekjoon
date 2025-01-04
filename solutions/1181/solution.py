import sys

words = set(sys.stdin.readlines()[1:])
sys.stdout.write("".join(sorted(words, key=lambda w: (len(w), w))))
