class Solution:
    def reverse(self, x: int) -> int:
        negLimit =-0x80000000
        posLimit = 0x7fffffff
        
        if (x > 0):
            
            reverseNum = int(str(x)[::-1])
            print (reverseNum)
            
            if reverseNum & posLimit == reverseNum:
                return reverseNum
            else:
                return 0
            
        elif (x < 0):
            
            reverseNum = -int(str(abs(x))[::-1])
            
            if reverseNum & negLimit == negLimit:
                return reverseNum
            else:
                return 0
        else:
            
            return 0
            
            
        