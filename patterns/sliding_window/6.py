# Longest Substring with Same Letters after Replacement
# -----
# - You are given a string "s" and an integer "k".
# - You can choose any character of the string and
# change it to any other uppercase English character.
# - You can perform this operation at most k times.
# - Return the length of the longest substring containing
# the same letter you can get after performing the above operations.
# -----
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# -----
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# -----
# Solution: https://leetcode.com/problems/longest-repeating-character-replacement/discuss/765776/Python%3A-Two-Pointers-%2B-Process-for-coding-interviews


import enum


def solution(s: str, k: int):
    left = 0
    char_freq = dict()
    longest_len = 0
    for right, _ in enumerate(s):

        if not s[right] in char_freq:
            char_freq[s[right]] = 0
        char_freq[s[right]] += 1

        # [Replacements cost] = [cells count between left and right] - [highest frequency]
        cells_count = right - left + 1
        if cells_count - max(char_freq.values()) <= k:
            longest_len = max(longest_len, cells_count)

        else:
            char_freq[s[left]] -= 1
            # if char_freq[s[left]] = 0 (=0 means False)
            if not char_freq[s[left]]:
                char_freq.pop(s[left])
            left += 1

    return longest_len


def main():
    # Test cases
    # Ouput(ABAB, 2): 4
    # Ouput(AABABBA, 1): 4
    # Ouput(BAAAABBA, 1): 5
    # Ouput(BAAAABBA, 3): 8
    # Ouput(BAAAABBBBBA, 1): 6
    # Ouput(CBAAAABBBBBA, 2): 6
    # Ouput(CBAAAABBBBBA, 1): 6
    # Ouput(CABAAAABBBBBA, 2): 7

    s, k = "BAAAABBA", 1
    res = solution(s, k)
    print(res)


main()
