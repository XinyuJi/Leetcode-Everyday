"""
Runtime: 28 ms, faster than 9.56% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.3 MB, less than 93.49% of Python online submissions for Letter Combinations of a Phone Number.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
        num = [''] if digits else []
        for d in digits:
            num = [a+b for a in num for b in dic[d]]
        return num
