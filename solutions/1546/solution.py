import sys

length = int(next(sys.stdin))
scores = list(map(int, sys.stdin.readline().split()))
sys.stdout.write(f"{sum(scores) / length / max(scores) * 100}")
