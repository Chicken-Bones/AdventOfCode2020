import re

if __name__ == "__main__":
    with open("input/day22.txt") as file:
        p1, p2 = file.read().split("\n\n")
        p1 = [int(s) for s in p1.strip().split("\n")[1:]]
        p2 = [int(s) for s in p2.strip().split("\n")[1:]]

        while p1 and p2:
            a, b = p1[0], p2[0]
            if a > b:
                p1 += [a, b]
            else:
                p2 += [b, a]
            p1 = p1[1:]
            p2 = p2[1:]

        win = p1 if p1 else p2
        print(sum((i+1)*c for i, c in enumerate(win[::-1])))

    with open("input/day22.txt") as file:
        p1, p2 = file.read().split("\n\n")
        p1 = [int(s) for s in p1.strip().split("\n")[1:]]
        p2 = [int(s) for s in p2.strip().split("\n")[1:]]

        def play(decks):
            seen = set()
            while all(decks):
                key = tuple(tuple(d) for d in decks)
                if key in seen:
                    return 0, None

                seen.add(key)
                cards = [d[0] for d in decks]
                decks = [d[1:] for d in decks]
                if all(c < len(d) for c, d in zip(cards, decks)):
                    win, _ = play([d[:c] for c, d in zip(cards, decks)])
                else:
                    win = 0 if cards[0] > cards[1] else 1

                decks[win] += [cards[win], cards[win^1]]

            return next((i, d) for i, d in enumerate(decks) if d)

        _, deck = play([p1, p2])
        print(sum((i+1)*c for i, c in enumerate(deck[::-1])))
