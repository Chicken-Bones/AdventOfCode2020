import re

if __name__ == "__main__":
    with open("input/day21.txt") as file:
        foods = []
        for l in file:
            _1, _2 = re.match(r"(.+?) \(contains (.+)\)", l).groups()
            foods.append((_1.split(" "), _2.split(", ")))

    all_allergens = set(a for _, allergens in foods for a in allergens)
    all_ingreds = set(i for ingreds, _ in foods for i in ingreds)
    potential_allergens = {i: [a for a in all_allergens if all(i in ingreds for ingreds, allergens in foods if a in allergens)] for i in all_ingreds}

    print(sum(not potential_allergens[i] for ingreds, _ in foods for i in ingreds))

    allergens_to_ingreds = {a: [i for i, allergens in potential_allergens.items() if a in allergens] for a in all_allergens}

    def apply(allergens, used_ingreds):
        if not allergens:
            return []

        a = allergens[0]
        for i in allergens_to_ingreds[a]:
            if i not in used_ingreds:
                if (r := apply(allergens[1:], used_ingreds + [i])) is not None:
                    return [(i, a)] + r

        return None


    ingred_allergens = apply(list(all_allergens), [])
    print(",".join(i for i, a in sorted(ingred_allergens, key=lambda kv: kv[1])))