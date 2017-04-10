import numpy
import copy
import math


class Solution:
    def __init__(self, n_stalls, n_people):
        self.n_stalls = n_stalls
        self.n_people = n_people
        
    def solute(self):
        num = self.n_stalls
        print num
        queue = {}
        top = [num, num]
        queue[top[0]] = 1
        while top[0] > 1:
            print top
            if top[0] == top[1]:
                child = list(self._birth(top[0], queue))
            else:
                child1 = list(self._birth(top[0], queue))
                child2 = list(self._birth(top[1], queue))
                child = list(set(child1 + child2))
            child.sort(reverse=True)
            if len(child) == 1:
                top = [child[0], child[0]]
            else: 
                top = [child[0], child[1]]
        print queue
        now_sum = 0
        for i in sorted(queue.keys(), reverse=True):
            now_sum += queue[i]
            print i, queue[i], now_sum
            if now_sum >= self.n_people:
                output = i
                break
        print output
        if output % 2 == 0:
            return output/2, output/2-1
        else:
            return output/2, output/2
        exit()
        
    def _birth(self, num, queue):
        child = []
        if num > 2:
            if num % 2 == 0:
                if num/2 not in queue:
                    queue[num/2] = 0
                queue[num/2] += queue[num]
                child.append(num/2)
                if num/2-1 not in queue:
                    queue[num/2-1] = 0
                queue[num/2-1] += queue[num]
                child.append(num/2-1)
            else:
                if num/2 not in queue:
                    queue[num/2] = 0
                queue[num/2] += 2 * queue[num]
                child.append(num/2)
        elif num == 2:
                if num/2 not in queue:
                    queue[num/2] = 0
                queue[num/2] += queue[num]
                child.append(num/2)
        return set(child)
        

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
        n_stalls, n_people = int(data[i][0]), int(data[i][1])
        i += 1
        solution = Solution(n_stalls, n_people)
        max_value, min_value = solution.solute()
        result.append('Case #%i: %i %i\n' % (n_result+1, max_value, min_value))
        print ('Case #%i: %i %i' % (n_result+1, max_value, min_value))
        n_result += 1
    with open('large.out.txt', 'w') as fw:
        for line in result:
            fw.writelines(line)
    
    
main()