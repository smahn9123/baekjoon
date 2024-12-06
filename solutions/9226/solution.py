vowels_list = ("a", "e", "i", "o", "u")
while True:
    s = input()
    if s == "#":
        break
    no_vowels = ""
    for c in s:
        if c in vowels_list:
            break
        else:
            no_vowels += c
    print(s[len(no_vowels) :] + no_vowels + "ay")
