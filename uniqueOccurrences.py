class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        
        l = []

        for i in set(arr):
            count = arr.count(i)
            
            if not count in l:
                l += [count]
            else:
                return False
        return True
            
s = Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))

