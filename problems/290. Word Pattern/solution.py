"""
https://leetcode.com/problems/word-pattern/description/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        # Go through the pattern and check
        # if the word matches the memoed
        # code.

        mem0, mem1 = {}, {}
        i = j = 0
        for c in pattern:
            if i >= len(s):
                # not enough words
                return False

            while j < len(s) and s[j] != ' ':
                j += 1

            word = s[i:j]

            if word in mem0:
                if mem0[word] != c:
                    return False
            else:
                mem0[word] = c

            if c in mem1:
                if mem1[c] != word:
                    return False
            else:
                mem1[c] = word

            i = j = j + 1
        return j >= len(s)
