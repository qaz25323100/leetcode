class Solution:
    def removeDuplicates(self, nums) -> int:
        curIdx = 0
        
        while curIdx < len(nums)-1:
            if nums[curIdx]==nums[curIdx+1]:
                del nums[curIdx+1]
                curIdx-=1
            curIdx+=1
            
        return len(nums)
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,2,2,3,3]))