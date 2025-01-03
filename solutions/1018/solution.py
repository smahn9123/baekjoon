import sys

m, n = map(int, next(sys.stdin).split())
board = [l.rstrip() for l in sys.stdin]


def get_num_of_flips_to_make_chess_board(i, j, start):
    count = 0
    correct = start
    for p in range(i, i + 8):
        for q in range(j, j + 8):
            if board[p][q] != correct:
                count += 1
            if q < j + 7:
                correct = "W" if correct == "B" else "B"
    return count


min_value = 32
for i in range(m - 7):
    for j in range(n - 7):
        w = get_num_of_flips_to_make_chess_board(i, j, "W")
        b = get_num_of_flips_to_make_chess_board(i, j, "B")
        min_value = min(min_value, w, b)

sys.stdout.write(f"{min_value}")
