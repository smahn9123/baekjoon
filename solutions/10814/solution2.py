import sys

sys.stdout.write(
    "\n".join(
        f"{i[0]} {i[1]}"
        for i in sorted(
            (
                (int(person.split()[0]), person.split()[1], index)
                for (index, person) in enumerate(sys.stdin.readlines()[1:])
            ),
            key=lambda x: (x[0], x[2]),
        )
    )
)
