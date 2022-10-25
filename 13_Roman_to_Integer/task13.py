TESTCASE = "MCMXCIV" # 1994

class Solution:
    def letterToNum(self, st: str) -> int:
        translator = {
            "I":1, 
            "V":5, 
            "X":10, 
            "L":50, 
            "C":100, 
            "D":500, 
            "M":1000
        }
        return translator[st]
    
    def romanToInt(self, s: str) -> int:
        count = 0
        lastNum = 0
        for char in s[::-1]:
            num = self.letterToNum(char)
            if num < lastNum:
                count -= num
                lastNum = num
                continue
            count += self.letterToNum(char)
            lastNum = num
        return count
            
res = Solution()
print(res.romanToInt(TESTCASE))
