# -*- encoding: gb18030
'''
406. Queue Reconstruction by Height

Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people in front of this person 
who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
'''
import random
import operator



class Solution(object):
    
    
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(self.cmp)
        print people
        recons_people = list()
        if len(people) >= 1 :
            recons_people.append(people[0])
            for term in people[1:] :
                n_geq, idx = 0, 0
                while True :
                    if n_geq == term[1] :
                        recons_people.insert(idx, term)
                        break
                    if recons_people[idx][0] >= term[0] :
                        n_geq += 1
                    idx += 1
            return recons_people
        else :
            return people
            
        
        
    def cmp(self, x, y):
        if x[0] < y[0] :
            return 1
        elif x[0] == y[0] :
            if x[1] > y[1] :
                return 1
            else :
                return -1
        else :
            return -1
        
        
    def constrcut(self, people):
        cons_people = list()
        for idx in range(len(people)) :
            k = 0
            for h in people[:idx] :
                if h >= people[idx] :
                    k += 1
            cons_people.append([people[idx], k]) 
        
        return cons_people


s = Solution()
# print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
people = s.constrcut([9,10,4,6])
print s.reconstructQueue(people)