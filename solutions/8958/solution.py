import sys

testcases = sys.stdin.readlines()[1:]
answer = []
for testcase in testcases:
    count = 0
    i = 0
    while i < len(testcase):
        if testcase[i] == "O":
            j = i + 1
            while j < len(testcase) and testcase[j] == "O":
                j += 1
            count += (j - i) * (j - i + 1) // 2
            i = j
        else:
            i += 1
    answer.append(str(count))
sys.stdout.write("\n".join(answer))
