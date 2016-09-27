# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == [] :
            return None
        while True :
            if len(lists) == 1 :
                return lists[0]
            new_list = list()
            for i in range(0, len(lists)-1, 2) :
                root = self.mergeTwoLists(lists[i], lists[i+1])
                new_list.append(root)
            if len(lists) % 2 != 0 :
                new_list.append(lists[-1])
            lists = new_list


    def mergeTwoLists(self, lista, listb) :
    	p, q = lista, listb
    	root, tail = None, None
    	while p != None and q != None :
    		if p.val <= q.val :
    			t = ListNode(p.val)
    			p = p.next
    		else :
    			t = ListNode(q.val)
    			q = q.next
    		if root == None :
    			root = t
    			tail = root
    		else :
    			tail.next = t
    			tail = tail.next
    	if p is None :
	    	while q != None :
	    		t = ListNode(q.val)
	    		q = q.next
	    		if root == None :
	    			root = t
	    			tail = root
	    		else :
	    			tail.next = t
	    			tail = tail.next

        if q is None :
	    	while p != None :
	    		t = ListNode(p.val)
	    		p = p.next
	    		if root == None :
	    			root = t
	    			tail = root
	    		else :
	    			tail.next = t
	    			tail = tail.next
        # self.printList(root)

        return root


    def printList(self, root) :
        t = root
        while t != None :
            print t.val,
            t = t.next
        print



s = Solution()
lists = [None, None, None, None]
r1 = ListNode(1)
r2 = ListNode(2)
r3 = ListNode(3)
lists[0] = r1
lists[0].next = r2
lists[0].next.next = r3

r1 = ListNode(4)
r2 = ListNode(5)
r3 = ListNode(6)
lists[1] = r1
lists[1].next = r2
lists[1].next.next = r3

r1 = ListNode(7)
r2 = ListNode(8)
r3 = ListNode(9)
lists[2] = r1
lists[2].next = r2
lists[2].next.next = r3
"""
r1 = ListNode(4)
r2 = ListNode(8)
r3 = ListNode(12)
lists[3] = r1
lists[3].next = r2
lists[3].next.next = r3
"""
root = s.mergeKLists(lists)
s.printList(root)
