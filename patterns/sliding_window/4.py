# Fruits into Baskets
# ------------------------------------
# You are visiting a farm that has a single row of fruit trees arranged from left to right.
# The trees are represented by an integer array "fruits" where "fruits[i]"
# is the type of fruit the "ith" tree produces
# You want to collect as much fruit as possible.
# There are some rules:
# - You only have 2 baskets, each basket can only hold a single type of fruit. There is
# no limit on the amount of fruit each basket can hold.
# - Starting from any tree of your choice, you must pick exactly one fruit from every tree while moving to the right.
# The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit cannot fit in your baskets, you must stop.

def solution(fruits):
    # Solution for this should be the same for question 3 but with k = 2
    table = dict()
    start = 0

    longest = 0

    for end in range(len(fruits)):
        newCharacter = fruits[end]

        if newCharacter in table.keys():
            table[newCharacter] += 1
        else:
            table[newCharacter] = 1

        while len(table) > 2:
            startCharacter = fruits[start]
            start += 1
            table[startCharacter] -= 1

            if table[startCharacter] == 0:
                table.pop(startCharacter)

        longest = max(longest, end - start + 1)

    return longest


def main():
    fruits = [0, 1, 2, 2]
    print(fruits)


main()
