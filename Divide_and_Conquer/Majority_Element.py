# -*- encoding: gb18030
'''
169. Majority Element

Given an array of size n, find the majority element. 
The majority element is the element that appears more than [n/2] times.
You may assume that the array is non-empty and the majority element always exist in the array.

'''

class Solution(object):
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = -1
        times = 0
        for num in nums :
            if times == 0 :
                majority = num
            if num == majority :
                times += 1
            else :
                times -= 1
                
        return majority
                

s = Solution()
print s.majorityElement([1,3,3,3,2,3,1])