if __name__ == "__main__":
    with open("input/day19.txt") as file:
        rules, cases = file.read().split("\n\n")
        rules = dict(s.split(": ") for s in rules.split("\n"))
        cases = cases.split("\n")

        def apply(r, s):
            if "|" in r:
                r1, _, r_tail = r.partition(" | ")
                return apply(r1, s) + apply(r_tail, s)

            if " " in r:
                r1, _, r_tail = r.partition(" ")
                return [v1+v2 for v1 in apply(r1, s) for v2 in apply(r_tail, s[len(v1):])]

            if r[0] == '"':
                text = r[1:-1]
                return [text] if s.startswith(text) else []

            return apply(rules[r], s)

        print(sum(s in apply("0", s) for s in cases))

        rules["8"] = "42 | 42 8"
        rules["11"] = "42 31 | 42 11 31"

        print(sum(s in apply("0", s) for s in cases))







