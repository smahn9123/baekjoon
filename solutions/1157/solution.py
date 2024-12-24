from collections import Counter

word = input().upper()
c = Counter(word)
most_common_2 = c.most_common(2)

match len(most_common_2):
    case 1:
        print(most_common_2[0][0])
    case 2:
        print(most_common_2[0][0] if most_common_2[0][1] > most_common_2[1][1] else "?")
