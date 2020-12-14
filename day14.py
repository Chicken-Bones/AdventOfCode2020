if __name__ == "__main__":
    with open("input/day14.txt") as file:
        mask = 0
        maskw = 0
        mem = [0] * (1 << 16)
        for s in file:
            if s.startswith("mask"):
                m = s[7:]
                mask = int(m.replace("1", "0").replace("X", "1"), 2)
                maskw = int(m.replace("X", "0"), 2)
            else:
                a, b = s.split(" = ")
                addr = int(a[4:-1])
                mem[addr] = (int(b) & mask) | maskw

        print(sum(mem))

    with open("input/day14.txt") as file:
        mask = 0
        maskw = 0
        mem = dict()
        for s in file:
            if s.startswith("mask"):
                m = s[7:]
                mask = int(m.replace("1", "0").replace("X", "1"), 2)
                maskw = int(m.replace("X", "0"), 2)
            else:
                a, b = s.split(" = ")
                addr = int(a[4:-1]) & ~mask | maskw

                # option A
                masks = [mask]
                while masks[-1] > 0:
                    masks += [m & (masks[-1]-1) for m in masks]

                for m in masks:
                    mem[m | addr] = int(b)

                # option B
                def write(m, addr):
                    if m == 0:
                        mem[addr] = int(b)
                    else:
                        write(m & (m-1), addr | m & -m)
                        write(m & (m-1), addr)

                write(mask, addr)

        print(sum(mem.values()))
