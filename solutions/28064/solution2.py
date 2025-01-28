import sys


def get_prefix_suffix_sets(name: str):
    prefixes = {name[:i] for i in range(1, len(name) + 1)}
    suffixes = {name[i:] for i in range(len(name))}
    return prefixes, suffixes


names = [name.strip() for name in sys.stdin.readlines()[1:]]
prefix_set = {}
suffix_set = {}

for name in names:
    prefix_set[name], suffix_set[name] = get_prefix_suffix_sets(name)

count = 0

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if (
            suffix_set[names[i]] & prefix_set[names[j]]
            or suffix_set[names[j]] & prefix_set[names[i]]
        ):
            count += 1

print(count)
