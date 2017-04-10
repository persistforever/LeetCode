import numpy
import copy
import math


class Solution:
    def __init__(self, num):
        self.num = num
        
    def solute(self):
        num_list = self._num2string(self.num)
        print num_list
        for i in range(len(num_list)-1, 0, -1):
            if num_list[i] < num_list[i-1]:
                for j in range(i, len(num_list)):
                    num_list[j] = 9
                num_list[i-1] -= 1
                print num_list
        return self._string2num(num_list)
        
    def _num2string(self, num):
        num_list = []
        while num > 0:
            num_list.append(num % 10)
            num /= 10
        num_list.reverse()
        return num_list
    
    def _string2num(self, num_list):
        result = 0
        for i in num_list:
            result = result * 10 + i
        return result
        

def import_file(path):
    data = []
    with open(path, 'r') as fo:
        for line in fo:
            data.append(line.strip().split(' '))
    return data

def main():
    data = import_file('large.txt')
    n_result, result = 1, []
    i = 0
    n_case = int(data[i][0])
    i += 1
    for _ in range(n_case):
        num = int(data[i][0])
        i += 1
        solution = Solution(num)
        res = solution.solute()
        result.append('Case #%i: %s\n' % (n_result, res))
        n_result += 1
    with open('large.out.txt', 'w') as fw:
        for line in result:
            fw.writelines(line)
    
    
main()