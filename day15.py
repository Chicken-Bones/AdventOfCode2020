if __name__ == "__main__":
    with open("input/day15.txt") as file:
        say_when = dict()
        turn = 0
        prev = None
        for s in file.read().split(","):
            say_when[prev] = turn
            prev = int(s)
            turn += 1

        while turn < 2020:
            next = turn - say_when[prev] if prev in say_when else 0
            say_when[prev] = turn
            prev = next
            turn += 1

        print(prev)

        while turn < 30000000:
            next = turn - say_when[prev] if prev in say_when else 0
            say_when[prev] = turn
            prev = next
            turn += 1

        print(prev)

