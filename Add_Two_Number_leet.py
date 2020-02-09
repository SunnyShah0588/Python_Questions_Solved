# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp = None
        prev = None
        carry = 0
        
        sumList = l1.val + l2.val
        print ("0",sumList)
        carry = 1 if sumList >= 10 else 0
        sumList = sumList if sumList < 10 else sumList % 10
        temp = ListNode(sumList)
        print ("1",temp)
        print ("2",sumList)
        
        L1 = l1.next
        L2 = l2.next
        L3 = temp
        
        print ("L1",L1)
        print ("L2",L2)
        
        while (L1 != None or L2 != None):           
            sumList = (L1.val if L1 else 0) + (L2.val if L2 else 0) + carry
            print ("3",sumList)
            carry = 1 if sumList >= 10 else 0
            sumList = sumList if sumList < 10 else sumList % 10
            print ("4",sumList)
            print ("5",carry)
            
            L3.next = ListNode(sumList)
            L3 = L3.next
            print (L3)
            
            L1 = L1.next if L1 else None
            L2 = L2.next if L2 else None
            
            print ("L1",L1)
            print ("L2",L2)
                
            if (carry > 0):
                L3.next = ListNode(carry)
            
            print ("temp",temp)
            
        if (carry > 0):
            temp.next = ListNode(carry)
        
        print ("Final",temp)
                
        return (L3)
                
            
            
            
            
        
        
        