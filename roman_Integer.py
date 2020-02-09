class Solution:
        
    def romanToInt(self, s: str) -> int:
        
        romInt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        integer = 0
        
        for i in range (len(s)):
            
            if i > 0 and romInt[s[i]] > romInt[s[i-1]]:
                integer += romInt[s[i]] - 2 * romInt[s[i-1]]
                
            else:
                integer += romInt[s[i]]
                
        return (integer)
                
                
                    
                    
        