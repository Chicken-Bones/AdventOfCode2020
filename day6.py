def allforgroup(s):
    group = s.strip().split('\n')
    return sum(all(q in p for p in group) for q in group[0])

if __name__ == "__main__":
    with open("input/day6.txt") as file:
        groups = file.read().split('\n\n')
        print(sum(len(set(s.replace('\n', ''))) for s in groups))
        print(sum(allforgroup(s) for s in groups))


