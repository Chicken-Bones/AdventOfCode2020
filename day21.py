import re

if __name__ == "__main__":
    with open("input/day21.txt") as file:
        foods = []
        for l in file:
            ingreds, allergens = re.match(r"(.+?) \(contains (.+)\)", l).groups()
            foods.append((set(ingreds.split(" ")), allergens.split(", ")))

    all_allergens = set(a for _, allergens in foods for a in allergens)
    allergens_to_ingreds = {a: set.intersection(*(ingreds for ingreds, allergens in foods if a in allergens)) for a in all_allergens}
    potential_allergens = set(i for ingreds in allergens_to_ingreds for i in ingreds)

    print(sum(i not in potential_allergens for ingreds, _ in foods for i in ingreds))

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