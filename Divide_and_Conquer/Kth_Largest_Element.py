# -*- encoding: gb18030
'''
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.
'''
import random


class Solution(object):    
    
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.k_largest = -1
        self.array = nums
        self.find_k_largest(0, len(nums)-1, k)
        
        return self.k_largest
        
        
    def find_k_largest(self, start, end, k) :
        pivot, m = self.partition(start, end)
        # print 'k=', k, 'm=', m, 'pivot=', pivot, 'array=', self.array[start: end+1]
        if m > k :
            self.find_k_largest(pivot+1, end, k)
        elif m < k :
            self.find_k_largest(start, pivot-1, k-m)
        else :
            self.k_largest = self.array[pivot]
        
        
    def partition(self, start, end) :
        pivot = start
        i, j = start+1, end
        while i < j :
            while i <= end and self.array[i] <= self.array[pivot] :
                i += 1
            while j >= (start+1) and self.array[j] > self.array[pivot] :
                j -= 1
            if i <= end and j >= (start+1) and i < j :
                self.array[i], self.array[j] = self.array[j], self.array[i]
        if self.array[pivot] > self.array[j] :
            self.array[pivot], self.array[j] = self.array[j], self.array[pivot]

        return j, end-j+1
    
                

s = Solution()
nums = range(1, 1000)
random.shuffle(nums)
print nums[0:1]
print s.findKthLargest(nums[0:1], 1)