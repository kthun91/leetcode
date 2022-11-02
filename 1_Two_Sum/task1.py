# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

nums = [3,3]
target = 6

class Solution:
    def twoSum(self, nums, target: int):    
        seen = {}
        for i, x in enumerate(nums):
            tmp = target - x
            if tmp in seen:
                return [seen[tmp], i]
            else:
                seen[x] = i 

res = Solution()
print(res.twoSum(nums, target))

