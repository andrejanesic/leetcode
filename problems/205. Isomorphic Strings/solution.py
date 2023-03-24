"""
https://leetcode.com/problems/isomorphic-strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False

        mapping = {}
        used = set()
        for i in range(n):
            c_s, c_t = s[i], t[i]
            print(c_s, c_t)
            if c_t in mapping:
                if c_s != mapping[c_t]:
                    return False
            else:
                if c_s in used:
                    return False
                mapping[c_t] = c_s
                used.add(c_s)
        return True
