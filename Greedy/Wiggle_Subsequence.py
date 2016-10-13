# -*- encoding: gb18030
'''
376. Wiggle Subsequence

A sequence of numbers is called a wiggle sequence 
if the differences between successive numbers strictly alternate between positive and negative. 
The first difference (if one exists) may be either positive or negative. 
A sequence with fewer than two elements is trivially a wiggle sequence.
For example, [1,7,4,9,2,5] is a wiggle sequence because 
the differences (6,-3,5,-7,3) are alternately positive and negative. 
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, 
the first because its first two differences are positive and the second because its last difference is zero.
Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. 
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, 
leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.
Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Input: [1,2,3,4,5,6,7,8,9]
Output: 2
'''
import random



class Solution(object):
    
    
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        if nums == list():
            return 0
        elif len(nums) == 1:
            return 1
        else :
            first, second = 0, 1
            while first < len(nums) - 1 and nums[second] == nums[first]:
                first += 1
                second += 1
            if first >= len(nums) - 1 :
                return 1
            operator = 1 if nums[second] > nums[first] else -1
            max_num = 2
            while first < len(nums) - 2:
                first += 1
                second += 1
                if nums[second] == nums[first]:
                    continue
                if operator > 0:
                    if nums[second] - nums[first] < 0:
                        max_num += 1
                        operator *= -1
                else :
                    if nums[second] - nums[first] > 0:
                        max_num += 1
                        operator *= -1
            return max_num
        
        
        
s = Solution()
print s.wiggleMaxLength([random.randint(1,10) for t in range(10000)])