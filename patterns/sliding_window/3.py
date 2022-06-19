# Longest Substring with K Distinct Characters (medium)
# -------------------------------------------------------
# Given a string you need to print the longest possible substring that has exactly M
# unique characters.
# If there are more than one substring ob longest possible length, then print any one of them.
# -------------------------------------------------------
# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
# TODO: https://medium.com/interviewnoodle/longest-substring-with-k-distinct-characters-in-python-sliding-window-pattern-coding-52e36fd79b96

def solution(string, k):
    # define a dictionary that will work as hash table to hold our
    # characters and their frequencies.
    table = dict()

    # two variables will point to the start and end of the window
    start = 0

    # variable to hold the size of the longest substring
    longest = 0

    # expand the window
    for end in range(len(string)):
        # get the new character
        newCharacter = string[end]

        # add the new character in the hash table
        if newCharacter in table.keys():
            table[newCharacter] += 1
        else:
            table[newCharacter] = 1

        # check if number of distinct characters in window is more
        # than K
        while len(table) > k:
            startCharacter = string[start]
            start += 1
            table[startCharacter] -= 1
            # if frequency becomes 0 then remove the character
            if table[startCharacter] == 0:
                table.pop(startCharacter)

        # check if current window is greatest seen so far
        longest = max(longest, end - start + 1)

    return longest


def main():
    string = "abababccc"
    k = 2
    # solution must be "aa", "bb", "cc"
    res = solution(string, k)
    print(res)


main()
