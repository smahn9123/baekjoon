# Checks continuity directly while traversing each word

n = int(input())
group_word_count = 0

for _ in range(n):
    word = input()
    is_group_word = True
    prev_char = None
    seen = set()

    for char in word:
        if char != prev_char:
            if char in seen:
                is_group_word = False
                break
            seen.add(char)
        prev_char = char

    if is_group_word:
        group_word_count += 1

print(group_word_count)
