def run_prog(instrs):
    acc = 0
    visited = [False] * len(instrs)
    ptr = 0

    while ptr < len(visited) and not visited[ptr]:
        visited[ptr] = True
        opcode, val = instrs[ptr]
        if opcode == "jmp":
            ptr += val
        else:
            if opcode == "acc":
                acc += val
            ptr += 1

    return acc, ptr


if __name__ == "__main__":
    with open("input/day8.txt") as file:
        instrs = [(s[:3], int(s[4:])) for s in file]
        print(run_prog(instrs)[0])

        for i in range(len(instrs)):
            inst, val = instrs[i]
            if inst == "acc":
                continue

            cpy = instrs.copy()
            cpy[i] = ("jmp" if inst == "nop" else "nop", val)
            acc, ptr = run_prog(cpy)
            if ptr == len(instrs):
                print(acc)
                break


