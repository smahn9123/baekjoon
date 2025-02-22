def is_pangram(s: str):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    character_set = set(c.lower() for c in s.lower() if c.lower() in alphabet_set)
    return "".join(sorted(alphabet_set - character_set))


n = int(input())
for _ in range(n):
    result = is_pangram(input())
    print(f"missing {result}" if result else "pangram")
