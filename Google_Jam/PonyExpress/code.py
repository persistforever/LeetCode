import numpy
import copy
from collections import OrderedDict


class Solution:
    def __init__(self, size):
        self.size = size
        self.map = numpy.zeros((self.size, self.size))-1
        self.horse = numpy.zeros((self.size, 2))
        
    def solute(self):
        print self.map
        self.distance = numpy.zeros((self.size, self.size))
        for i in range(self.size):
            for j in range(self.size):
                self.distance[i,j] = 0.0
                for k in range(i,j):
                    self.distance[i,j] += self.map[k,k+1]
        print self.distance
        self.times = numpy.zeros((self.size, self.size))
        for i in range(1, self.size):
            for j in range(0, i):
                print i, j
                print self.distance[j,i]
                if self.horse[j][0] < self.distance[j,i]:
                    self.times[i,j] = 0
                else:
                    print 'max_top', self.times[i-1,0:j+1]
                    self.times[i,j] = min(self.times[i-1,0:j+1]) +  self.map[i-1,i] / self.horse[j][1]
            self.times[i,i] = 
        print self.times

def import_file(path):
    data = []
    with open(path, 'r') as fo:
        for line in fo:
            data.append(line.strip().split(' '))
    return data

def main():
    data = import_file('test.txt')
    n_result, result = 0, []
    i = 0
    n_case = int(data[i][0])
    i += 1
    for _ in range(n_case):
        size, pos = int(data[i][0]), int(data[i][1])
        i += 1
        solution = Solution(size)
        for j in range(size):
            solution.horse[j][0] = int(data[i][0])
            solution.horse[j][1] = int(data[i][1])
            i += 1
        for j in range(size):
            solution.map[j,:] = [int(t) for t in data[i]]
            i += 1
        time = solution.solute()
        print time
        result.append('Case #%i: %.6f\n' % (n_result+1, time))
        n_result += 1
    with open('test.out.txt', 'w') as fw:
        for line in result:
            fw.writelines(line)
    
    
main()