import numpy
import copy


class Solution:
    def __init__(self, distance):
        self.distance = distance
        self.horse_list = []
        
    def add_horse(self, start, speed):
        self.horse_list.append([start, speed])
        
    def solute(self):
        max_time = 0 
        for start, speed in self.horse_list:
            time = 1.0 * (self.distance - start) / speed
            if time >= max_time:
                max_time = time
                
        return self.distance / max_time

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
        distance, n_horse = int(data[i][0]), int(data[i][1])
        i += 1
        solution = Solution(distance)
        for _ in range(n_horse):
            start, speed = int(data[i][0]), int(data[i][1])
            i += 1
            solution.add_horse(start, speed)
        my_speed = solution.solute()
        print my_speed
        result.append('Case #%i: %.6f\n' % (n_result+1, my_speed))
        n_result += 1
    with open('large.out.txt', 'w') as fw:
        for line in result:
            fw.writelines(line)
    
    
main()