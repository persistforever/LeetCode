# -*- encoding: gb18030
'''
55. Jump Game

Given an array of non-negative integers, 
you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''
import random



class Solution(object):
    
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        for i in range(len(nums)-1) :
            if i > max_pos :
                break
            max_pos = max(max_pos, i+nums[i])
            
        return max_pos >= len(nums)-1
        
        
        
s = Solution()
print s.canJump([1, 3, 0, 4, 1])