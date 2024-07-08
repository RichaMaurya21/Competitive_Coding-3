#Find pairs
class Solution:
    def findPairs(self, nums, k):
        numDict = {}
        count = 0
        for num in nums:
            numDict[num] = numDict.get(num,0) + 1

        for num in numDict:
            if k == 0:
                if numDict[num] > 1:
                    count += 1

            else:
                if num + k in numDict:
                    count += 1
            
        return count


sol = Solution()
nums = [1,3,1,5,4]
k = 0
print(sol.findPairs(nums,k))