# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        ret = temp = ListNode(0)
        carry = 0
        sumList = 0
        
        while (l1 or l2 or carry):
            
            v1 = v2 = 0
            
            if l1 != None:
                v1 = l1.val
                l1 = l1.next
                
            if l2 != None:
                v2 = l2.val
                l2 = l2.next
                
                
                
            sumList = v1 + v2 + carry
            carry = sumList // 10
            sumList = sumList if sumList < 10 else sumList % 10
            
            temp.next = ListNode(sumList)
            temp = temp.next
            
            print ("In Loop ",temp)
            
        print ("Out Loop",temp)
        print ("ret",ret)
        return ret.next