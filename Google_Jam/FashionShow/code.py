import numpy
import copy


class Solution:
    def __init__(self, size):
        self.size = size
        self.plus_map = numpy.zeros((self.size, self.size), dtype=int)
        self.cross_map = numpy.zeros((self.size, self.size), dtype=int)
        self.plus_max = 0
        self.cross_max = 0
        self.final_plus_map = None
        self.final_cross_map = None
        
    def add_point(self, type, x, y):
        x, y = x-1, y-1
        if type == '+':
            self.plus_map[x, y] = 1
        elif type == 'x':
            self.cross_map[x, y] = 1
        elif type == 'o':
            self.plus_map[x, y] = 1
            self.cross_map[x, y] = 1
            
    def solute(self):
        cross_map, plus_map = copy.deepcopy(self.cross_map), copy.deepcopy(self.plus_map)
        self._recursive_plus()
        self._recursive_cross()
        print '='*20
        n_add, add_list = 0, []
        for x in range(self.size):
            for y in range(self.size):
                if cross_map[x, y] == 1 and plus_map[x, y] == 0 and \
                    self.final_cross_map[x, y] == 1 and self.final_plus_map[x, y] == 1:
                    n_add += 1
                    add_list.append(['o', x+1, y+1])
                elif cross_map[x, y] == 0 and plus_map[x, y] == 1 and \
                    self.final_cross_map[x, y] == 1 and self.final_plus_map[x, y] == 1:
                    n_add += 1
                    add_list.append(['o', x+1, y+1])
                elif cross_map[x, y] == 0 and plus_map[x, y] == 0 and \
                    self.final_cross_map[x, y] == 1 and self.final_plus_map[x, y] == 0:
                    n_add += 1
                    add_list.append(['x', x+1, y+1])
                elif cross_map[x, y] == 0 and plus_map[x, y] == 0 and \
                    self.final_cross_map[x, y] == 0 and self.final_plus_map[x, y] == 1:
                    n_add += 1
                    add_list.append(['+', x+1, y+1])
                elif cross_map[x, y] == 0 and plus_map[x, y] == 0 and \
                    self.final_cross_map[x, y] == 1 and self.final_plus_map[x, y] == 1:
                    n_add += 1
                    add_list.append(['o', x+1, y+1])
        
        return self.cross_max + self.plus_max, n_add, add_list
        
    def _recursive_plus(self):
        valid_map = numpy.zeros((self.size, self.size), dtype=int)
        for x in range(self.plus_map.shape[0]):
            for y in range(self.plus_map.shape[1]):
                if self.plus_map[x, y] == 1:
                    self._set_valid_plus(x, y, valid_map)
        point_list = self._get_sorted_point_list()
        while self._can_add(valid_map):
            for point, score in point_list:
                [x, y] = point
                if valid_map[x, y] == 0:
                    self.plus_map[x, y] = 1
                    self._set_valid_plus(x, y, valid_map)
        self.final_plus_map = self.plus_map
        self.plus_max = self.final_plus_map.sum().sum()
        print self.plus_max, self.final_plus_map
    
    def _get_sorted_point_list(self):
        point_list = []
        for x in range(self.plus_map.shape[0]):
            for y in range(self.plus_map.shape[1]):
                score = 0
                new_x, new_y = x, y
                while 0 <= new_x < self.size and 0 <= new_y < self.size:
                    new_x -= 1
                    new_y -= 1
                    score += 1
                new_x, new_y = x, y
                while 0 <= new_x < self.size and 0 <= new_y < self.size:
                    new_x -= 1
                    new_y += 1
                    score += 1
                new_x, new_y = x, y
                while 0 <= new_x < self.size and 0 <= new_y < self.size:
                    new_x += 1
                    new_y -= 1
                    score += 1
                new_x, new_y = x, y
                while 0 <= new_x < self.size and 0 <= new_y < self.size:
                    new_x += 1
                    new_y += 1
                    score += 1
                point_list.append([[x, y], score])
        return sorted(point_list, key=lambda x: x[1], reverse=False)
    
    def _set_valid_plus(self, x, y, valid_map):
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_x -= 1
            new_y -= 1
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_x -= 1
            new_y += 1
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_x += 1
            new_y -= 1
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_x += 1
            new_y += 1
        
    def _recursive_cross(self):
        valid_map = numpy.zeros((self.size, self.size), dtype=int)
        for x in range(self.cross_map.shape[0]):
            for y in range(self.cross_map.shape[1]):
                if self.cross_map[x, y] == 1:
                    self._set_valid_cross(x, y, valid_map)
        self._sub_recursive_cross(self.cross_map, valid_map)
        if self.final_cross_map is None:
            self.final_cross_map = self.cross_map
        self.cross_max = self.final_cross_map.sum().sum()
        print self.cross_max, self.final_cross_map
        
    def _sub_recursive_cross(self, cross_map, valid_map):
        while self._can_add(valid_map):
            for x in range(valid_map.shape[0]):
                for y in range(valid_map.shape[1]):
                    if valid_map[x, y] == 0:
                        cross_map[x, y] = 1
                        self._set_valid_cross(x, y, valid_map)
        self.final_cross_map = cross_map
            
    def _can_add(self, valid_map):
        can_add = False
        for x in range(valid_map.shape[0]):
            for y in range(valid_map.shape[1]):
                if valid_map[x, y] == 0:
                    can_add = True
                    return can_add
            
        return can_add
    
    def _set_valid_cross(self, x, y, valid_map):
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_x -= 1
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_x += 1
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_y -= 1
        new_x, new_y = x, y
        while 0 <= new_x < self.size and 0 <= new_y < self.size:
            valid_map[new_x, new_y] = 1
            new_y += 1
        

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
        size, n_init = int(data[i][0]), int(data[i][1])
        i += 1
        solution = Solution(size)
        for _ in range(n_init):
            type, x, y = data[i][0], int(data[i][1]), int(data[i][2])
            i += 1
            solution.add_point(type, x, y)
        y, z, l = solution.solute()
        print y, z, l
        result.append('Case #%i: %i %i\n' % (n_result+1, y, z))
        for model, posx, posy in l:
            result.append('%s %i %i\n' % (model, posx, posy))
        n_result += 1
    with open('large.out.txt', 'w') as fw:
        for line in result:
            fw.writelines(line)
    
    
main()