import sys

lines = sys.stdin.readlines()
cards = lines[1].split()
questions = lines[3].split()
cards_map = {card: True for card in cards}

sys.stdout.write(" ".join("1" if cards_map.get(q, None) else "0" for q in questions))
