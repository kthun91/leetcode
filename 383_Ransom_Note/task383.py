ransomNote = "aa"
magazine = "aab"

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for elem in ransomNote:
            try:
                magazine.remove(elem)
            except: 
                return False
        return True

res = Solution()
print(res.canConstruct(ransomNote, magazine))
