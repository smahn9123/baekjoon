import sys

gradeTable = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total_hours = 0
total_score = 0
for line in sys.stdin:
    _subject, hours, grade = line.split()
    if grade == "P":
        continue
    total_hours += float(hours)
    total_score += float(hours) * gradeTable[grade]

sys.stdout.write(f"{total_score / total_hours:6f}")
