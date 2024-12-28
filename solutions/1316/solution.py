import sys

words = [line.rstrip() for line in sys.stdin.readlines()][1:]


def is_word_grouped(word):
    chars = set(word)
    for char in chars:
        indices = [i for i, c in enumerate(word) if char == c]
        is_c_grouped = indices[-1] - indices[0] == len(indices) - 1
        if not is_c_grouped:
            return False
    return True


grouped_word_count = 0
for word in words:
    if is_word_grouped(word):
        grouped_word_count += 1

sys.stdout.write(f"{grouped_word_count}")
