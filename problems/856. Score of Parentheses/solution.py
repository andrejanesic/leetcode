"""
https://leetcode.com/problems/score-of-parentheses/description/

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: s = "()"
Output: 1

Example 2:
Input: s = "(())"
Output: 2

Example 3:
Input: s = "()()"
Output: 2
 

Constraints:
2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
"""

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        parentheses = []
        score = []
        res = 0
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                parentheses.append(c)
                score.append(0)
                continue
            if c == ")" and parentheses and parentheses[-1] == "(":
                parentheses.pop()
                t = score.pop()
                if t == 0:
                    t = 1
                else:
                    t *= 2
                if not score:
                    res += t
                else:
                    score[-1] += t
        return int(res)
