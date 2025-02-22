import sys

book_sales = {}

for book in sys.stdin.readlines()[1:]:
    book = book.rstrip()
    if book in book_sales:
        book_sales[book] += 1
    else:
        book_sales[book] = 0

max_sales = max(book_sales.values())
best_sellers = [book for book, sales in book_sales.items() if sales == max_sales]
print(sorted(best_sellers)[0])
