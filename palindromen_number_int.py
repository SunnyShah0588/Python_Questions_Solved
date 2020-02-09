class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if (x > 0):
            temp = x
            rev = 0
            
            while x > 0:
                digit = x % 10
                rev = rev * 10 + digit
                x = x // 10
                
            if (temp == rev):
                return True
            
            else:
                return False
            
        elif (x < 0):
            
            return False
        
        elif (x == 0):
            
            return True
            
            
        
        