import numpy
import copy
from collections import OrderedDict


class Solution:
    def __init__(self, n, r, o, y, g, b, v):
        self.n = n
        self.r = r
        self.o = o
        self.y = y
        self.g = g
        self.b = b
        self.v = v
        
    def solute(self):
        color_dict = OrderedDict()
        index_list = sorted(enumerate([self.r, self.y, self.b]), key=lambda x: x[1], reverse=True)
        for color_index, number in index_list:
            color_dict[['R', 'Y', 'B'][color_index]] = number
        str = ''
        last_color = -1
        for i in range(self.n):
            temp_color_dict = copy.deepcopy(color_dict)
            if last_color != -1:
                del temp_color_dict[last_color]
                if sum(temp_color_dict.values()) == 0:
                    break
            color = max(temp_color_dict.iteritems(), key=lambda x: x[1])[0]
            str += color
            color_dict[color] -= 1
            last_color = color
        if i < self.n-1:
            return 'IMPOSSIBLE'
        else:
            if str[0] == str[-1]:
                return 'IMPOSSIBLE'
            else:
                return str

def import_file(path):
    data = []
    with open(path, 'r') as fo:
        for line in fo:
            data.append(line.strip().split(' '))
    return data

def main():
    data = import_file('large.txt')
    n_result, result = 0, []
    i = 0
    n_case = int(data[i][0])
    i += 1
    for _ in range(n_case):
        [n, r, o, y, g, b, v] = [int(t) for t in data[i]]
        i += 1
        solution = Solution(n, r, o, y, g, b, v)
        str = solution.solute()
        print str
        result.append('Case #%i: %s\n' % (n_result+1, str))
        n_result += 1
    with open('large.out.txt', 'w') as fw:
        for line in result:
            fw.writelines(line)
    
    
main()