import sys

card_count = {}
lines = sys.stdin.readlines()
for card in lines[1].split():
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

sys.stdout.write(
    " ".join(
        str(card_count[query]) if query in card_count else "0"
        for query in lines[3].split()
    )
)
