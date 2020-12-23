import operator
from functools import reduce


def parse_class(s):
    name, _, ranges = s.partition(": ")
    return name, [tuple(int(i) for i in r.split("-")) for r in ranges.split(" or ")]


def in_range(v, ranges):
    return any(low <= v <= high for low, high in ranges)


if __name__ == "__main__":
    with open("input/day16.txt") as file:
        fields, myticket, tickets = file.read().split("\n\n")
        tickets = tickets.strip().split("\n")[1:]
        tickets = [[int(s) for s in ticket.split(",")] for ticket in tickets]

        myticket = [int(s) for s in myticket.split("\n")[1].split(",")]

        fields = dict(parse_class(s) for s in fields.split("\n"))

        all_values = [v for ticket in tickets for v in ticket]
        fake_values = [v for v in all_values if all(not in_range(v, ranges) for ranges in fields.values())]

        print(sum(fake_values))

        tickets = [t for t in tickets if not any(v in fake_values for v in t)]

        ordered_fields = [None] * len(fields)
        possible_match = {i: [name for name, ranges in fields.items() if all(in_range(t[i], ranges) for t in tickets)] for i in range(len(fields))}
        while possible_match:
            next_i, fs = min(possible_match.items(), key=lambda kv: len(kv[1]))
            f = fs[0]
            ordered_fields[next_i] = f
            del possible_match[next_i]
            for v in possible_match.values():
                v.remove(f)

        depts = [myticket[i] for i, name in enumerate(ordered_fields) if name.startswith("departure")]
        print(reduce(operator.mul, depts, 1))