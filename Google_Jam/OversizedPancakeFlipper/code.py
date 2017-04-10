import numpy
import copy
import math


class Solution:
    def __init__(self, string, k):
        self.string = [t for t in string]
        self.k = k
        
    def solute(self):
        reverse_dict = {'+': '-', '-': '+'}
        max_pos = len(self.string)
        now_pos = 0
        now_string = self.string
        n_reverse = 0
        while max_pos - now_pos >= self.k:
            if now_string[now_pos] == '-':
                for i in range(self.k):
                    now_string[now_pos+i] = reverse_dict[now_string[now_pos+i]]
                n_reverse += 1
                now_pos += 1
            else:
                now_pos += 1
        if '-' in now_string:
            return 'IMPOSSIBLE'
        else:
            return str(n_reverse)
        

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
        string, k = data[i][0], int(data[i][1])
        i += 1
        solution = Solution(string, k)
        res = solution.solute()
        result.append('Case #%i: %s\n' % (n_result, res))
        n_result += 1
    with open('large.out.txt', 'w') as fw:
        for line in result:
            fw.writelines(line)
    
    
main()