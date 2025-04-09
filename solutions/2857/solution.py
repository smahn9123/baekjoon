import sys

found = False
for order, codename in enumerate(sys.stdin, start=1):
    if codename.find("FBI") != -1:
        sys.stdout.write(str(order) + " ")
        found = True
if not found:
    sys.stdout.write("HE GOT AWAY!")
