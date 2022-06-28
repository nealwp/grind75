"""
Problem:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order

v1:
    -- make a dict of 'closers'
    -- iterate through the list and compare element and element+1 
        to it's 'closer'
    -- skip any element where the left paren is not in the dict keys
    -- return false on failure, or true if list complete and no failures

    ** this failed on '{[]}', need to handle nested **
"""
class Solution:
    def isValid(self, s: str) -> bool:
        closer = { "(": ")", "[": "]", "{": "}" }
        for idx, char in enumerate(s):
            if char in closer.keys() and s[idx+1] != closer[char]:
                return False
            else:
                continue
        return True

"""
v2:
    -- use the dict again
    -- just search if there's closer after the current element
    -- if not, return false

    ** this fails on '([)]'
"""
class Solution:
    def isValid(self, s: str) -> bool:
        closer = { "(": ")", "[": "]", "{": "}" }
        current_open = None
        for char in s:
            if char in closer.keys():
                current_open = char
                continue
            if char not in closer.keys() and char != closer[current_open]:
                return False      
        return True

"""
v3:
    -- iterate through string
    -- if opener, push into an array
    -- if closer, compare last element in opener array
        -- if match, pop out of array
        -- if not match, return false and exit
    -- return true if list exhausted
"""
class Solution:
    def isValid(self, s: str) -> bool:
        closer = { "(": ")", "[": "]", "{": "}" }
        opener_list = []
        for char in s:
            if char in closer.keys():
                opener_list.append(char)
                continue
            if char not in closer.keys() and len(opener_list) > 0:
                if closer[opener_list[-1]] == char:
                    opener_list.pop()
                    continue
                if not closer[opener_list[-1]] == char:
                    return False
            else:
                return False
        if len(opener_list) == 0:
            return True
        return False

"""
Results:
Runtime: 47 ms, faster than 51.09% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 69.40% of Python3 online submissions for Valid Parentheses.
"""