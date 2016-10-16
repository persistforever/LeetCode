# -*- encoding: gb18030
'''
402. Remove K Digits

Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.
Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''
import random



class Solution(object):
    
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == 0:
            return '0'
        print num
        stack = list()
        del_num = [0]*len(num)
        n = k
        for idx, term in enumerate(num):
            while stack != list() and n > 0 and term < stack[-1]:
                stack.pop()
                n -= 1 
            stack.append(term)
        print stack, n
        for i in range(len(stack)):
            if stack[i] != '0':
                break
        result = ''.join(stack[i:len(num)-n-i])
        if result == '':
            return '0'
        else:
            return result
        
        
s = Solution()
num = '222312'
k = 2
print s.removeKdigits(num, k)
print len(num) - k