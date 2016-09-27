# -*- encoding: gb18030
'''
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property,  
where counts[i] is the number of smaller elements to the right of nums[i].

Example:
Given nums = [5, 2, 6, 1]
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''
import random



class Solution(object):
    
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == [] :
            return []
        self.array = zip(nums, range(len(nums)))
        self.sorted_array = [None] * len(self.array)
        self.count = [0] * len(self.array)
        self.mergeSort(0, len(self.array)-1)
        
        return self.count
        
        
    def mergeSort(self, start, end):
        mid = (start + end) / 2
        if start != end :
            self.mergeSort(start, mid)
            self.mergeSort(mid+1, end)
            self.merge(start, mid, end)
        else :
            self.merge(start, mid, end)
        
        
    def merge(self, start, mid, end):
        # print self.array[start: end+1]
        i, j, t = start, mid+1, start
        # print start, mid, end, i, j, t
        while i <= mid and j <= end :
            if self.array[i][0] <= self.array[j][0] :
                self.sorted_array[t] = self.array[i]
                self.count[self.array[i][1]] += j - mid - 1
                i += 1
            else :
                self.sorted_array[t] = self.array[j]
                j += 1
            t += 1
        if i > mid :
            while j <= end :
                self.sorted_array[t] = self.array[j]
                j += 1
                t += 1
        elif j > end :
            while i <= mid :
                self.sorted_array[t] = self.array[i]
                self.count[self.array[i][1]] += j - mid - 1
                i += 1
                t += 1
        # print self.sorted_array[start: end+1]
        self.array[start: end+1] = self.sorted_array[start: end+1]
        

n = 5
nums = list()
for _ in range(n) :
    nums.append(random.randint(0,n))
random.shuffle(nums)
print nums
s = Solution()
s.countSmaller(nums)
print s.sorted_array
print s.count
