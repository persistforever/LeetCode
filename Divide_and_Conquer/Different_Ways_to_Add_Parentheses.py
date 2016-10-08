# -*- encoding: gb18030
'''
241. Different Ways to Add Parentheses

Given a string of numbers and operators, 
return all possible results from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1
Input: "2-1-1".
((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]

Example 2
Input: "2*3-4*5"
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''

import random
import re



class Solution(object):
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        result = self.tokenizer(input)
        
        return sorted(result)
        
    
    def tokenizer(self, input) :
        array = re.split('([*+-])', input)
        
        return self.subCompute(array)
            
            
    def subCompute(self, array) :
        if len(array) == 1 :
            return [int(array[0])]
        elif len(array) == 3 :
            return [self.compute(array[0], array[1], array[2])]
        else :
            result = list()
            for i in range(len(array)-2, 0, -2) :
                print i
                left = self.subCompute(array[0:i])
                right = self.subCompute(array[i+1:])
                for first in left :
                    for second in right :
                        result.append(self.compute(first, array[i], second))
            return result
            
        
    def compute(self, first, operator, second) :
        if operator == '+' :
            return int(first) + int(second)
        elif operator == '-' : 
            return int(first) - int(second)
        elif operator == '*' : 
            return int(first) * int(second)
        
        
s = Solution()
s.diffWaysToCompute('2*3-4*5')
        