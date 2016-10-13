# -*- encoding: gb18030
'''
45. Jump Game II

Given an array of non-negative integers, 
you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. 
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
import random



class Solution(object):
    
    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == list() or len(nums) == 1 :
            return 0
        else :
            max_pos = 0 + nums[0]
            n_step = 0
            i = 0
            while True :
                n_step += 1
                if max_pos >= len(nums) - 1 :
                    break
                for i in range(i, max_pos+1) :
                    max_pos = max(max_pos, i+nums[i])
            return n_step
        
        
        
s = Solution()
print [random.randint(1,1) for t in range(100000)]
print s.jump([1]*100000)