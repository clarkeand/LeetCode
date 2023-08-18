"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) == 1:
            return s

        longest_palindrome = ""
        for i in range(len(s)):
            palindrome1 = expand_around_center(i, i)
            palindrome2 = expand_around_center(i, i + 1)

            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2

        return longest_palindrome