"""
Problem:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and
    removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric
    characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
v1:
    -- strip all non alpha numerics and covert to lowercase
    -- convert string to list
    -- copy the list
    -- reverse the copy
    -- test equality
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = ''
        for char in s:
            if str.isalnum(char):
                stripped_s += char.lower()
        list1 = list(stripped_s)
        list2 = list(stripped_s)
        list2.reverse()
        return list1 == list2
"""
Results:
Runtime: 54 ms, faster than 82.42% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.3 MB, less than 22.79% of Python3 online submissions for Valid Palindrome.
"""