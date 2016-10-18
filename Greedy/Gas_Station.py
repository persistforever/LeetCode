# -*- encoding: gb18030
'''
134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and 
it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once, 
otherwise return -1.
Note:
The solution is guaranteed to be unique.
'''
import random



class Solution(object):
    
    
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sub = list()
        for g, c in zip(gas, cost):
            sub.append(g-c)
        sub = sub + sub[0:-1]
        start, end, whole_sum, around = 0, 0, 0, False
        while start < len(gas):
            if end - start > len(gas) and whole_sum >= 0:
                around = True
                break
            if start > end:
                end = start
                whole_sum = 0
            whole_sum = sum(sub[start:end+1])
            if whole_sum >= 0:
                end += 1
            else:
                start += 1
        
        if around:
            return start
        else:
            return -1
        
        
s = Solution()
n = 10000
gas = [random.randint(1,9) for i in range(n)]
cost = [random.randint(1,9) for i in range(n)]
print gas
print cost
# print s.canCompleteCircuit(gas, cost)