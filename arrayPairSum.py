class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums = sorted(nums)

        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]

        return res

s = Solution()
s.arrayPairSum([1,4,3,2])