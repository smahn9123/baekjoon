import sys

input = sys.stdin.readline
t = int(input())
sys.stdout.write("\n".join(f"{sum(map(int, input().split(',')))}" for _ in range(t)))
