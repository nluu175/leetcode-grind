'''
--- No Repeat Substring
Problem Statement 
Given a string, find the length of the longest substring which has no repeating characters.
Example 1:
Input: String="aabccbb"
--- Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:
Input: String="abbbb"
--- Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:
Input: String="abccde"
--- Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''


def solution(string):
    # table is used to stored the latest index of character "x"
    table = dict()
    left = 0
    longest = 0
    for right, item in enumerate(string):
        if item in table:
            left = right

        table[item] = right
        longest = max(longest, right - left + 1)
        print((left, right))

    print(f"longest: {longest}")


def main():
    string = "aabccbb"
    # string = "abbbb"
    # string = "abccde"
    solution(string)


main()
