"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, res_s, res_e = 1, 0, 0

        for center in range(len(s) * 2 - 1):
            start = center // 2
            end = (center + center % 2) // 2
            l = center % 2 - 1

            i = 0
            while start - i >= 0 and end + i < len(s) and s[start - i] == s[end + i]:
                i += 1
                l += 2

            if l > res:
                res = l
                res_s = start - i + 1
                res_e = end + i - 1
        return s[res_s: res_e + 1]
