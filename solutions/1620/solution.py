import sys

n, m = map(int, sys.stdin.readline().split())
pokedex = {}
for i in range(1, n + 1):
    pokemon_name = sys.stdin.readline().rstrip()
    pokedex[pokemon_name] = str(i)
    pokedex[str(i)] = pokemon_name
for _ in range(m):
    q = sys.stdin.readline().rstrip()
    sys.stdout.write(pokedex[q] + "\n")
