# -*- encoding: gb18030
'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Given target = 5, return true.
Given target = 20, return false.
'''
import random


class Solution(object):
    
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.matrix = matrix
        self.target = target
        self.finded = False
        if self.matrix != [] :
            n_rows = len(self.matrix)
            if n_rows != 0 :
                n_cols = len(self.matrix[0])
            else :
                n_cols = 0
            self.searchSubMatrix(0, n_rows-1, 0, n_cols-1)
            
        return self.finded
        
        
    def searchSubMatrix(self, row_start, row_end, col_start, col_end):
        # self.printSubMatrix(row_start, row_end, col_start, col_end)
        if row_start == row_end and col_start == col_end :
            if self.matrix[row_start][col_start] == self.target :
                self.finded = True
            return
        row_mid = (row_start + row_end) / 2
        col_mid = (col_start + col_end) / 2
        if self.matrix[row_mid][col_mid] == self.target :
            self.finded = True
        elif self.matrix[row_mid][col_mid] > self.target :
            self.searchSubMatrix(row_start, row_mid, col_start, col_mid)
            if self.finded == False :
                self.searchSubMatrix(row_start, row_mid, min(col_mid+1, col_end), col_end)
            if self.finded == False :
                self.searchSubMatrix(min(row_mid+1, row_end), row_end, col_start, col_mid)
        else :
            self.searchSubMatrix(row_start, row_mid, min(col_mid+1, col_end), col_end)
            if self.finded == False :
                self.searchSubMatrix(min(row_mid+1, row_end), row_end, col_start, col_mid)
            if self.finded == False :
                self.searchSubMatrix(min(row_mid+1, row_end), row_end, min(col_mid+1, col_end), col_end)
                
                
    def printSubMatrix(self, row_start, row_end, col_start, col_end):
        print row_start, row_end, col_start, col_end
        for i in range(row_start, row_end+1) :
            for j in range(col_start, col_end+1) :
                print self.matrix[i][j],
            print 
        print 
        
        
s = Solution()
print s.searchMatrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], 5)