"""
https://leetcode.com/problems/find-all-anagrams-in-a-string

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        self.sol = []
        self.foundStore = {}
        self.subLen = 0
        self.anagramLetters = set()
        self.anagramLettersReq = {}

        # Fetch the frequency for each letter and create a hash
        # set of letters for faster indexing
        for i in range(len(p)):
            ch = p[i]
            self.anagramLetters.add(ch)
            if not (ch in self.anagramLettersReq):
                self.anagramLettersReq[ch] = 1
            else:
                self.anagramLettersReq[ch] += 1
            if not (ch in self.foundStore):
                self.foundStore[ch] = 0

        # Each time we add a letter, check if it's an anagram
        # letter, and if yes, check if requirements are already
        # fulfilled for this letter. If not, add it in and increase
        # the count - otherwise, leave it out.
        def addLetter(l: str) -> bool:
            if not l in self.anagramLetters:
                return
            self.foundStore[l] += 1
            if self.foundStore[l] > self.anagramLettersReq[l]:
                return False
            if self.foundStore[l] == self.anagramLettersReq[l]:
                self.subLen += 1
            if self.subLen == len(self.anagramLetters):
                return True
            return False

        # Each time we remove a letter, check if it's an anagram
        # letter, and if yes, check if removing it breaks the
        # requirements. If yes, decrease the count.
        def remLetter(l: str) -> None:
            if not l in self.anagramLetters:
                return
            if self.foundStore[l] == self.anagramLettersReq[l]:
                self.subLen -= 1
            self.foundStore[l] -= 1

        for i in range(len(s) - 1, -1, -1):
            toRem = i + len(p)
            if toRem <= len(s) - 1:
                remLetter(s[toRem])
            if addLetter(s[i]):
                self.sol.append(i)

        return self.sol
