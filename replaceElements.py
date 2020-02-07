class Solution:
    def replaceElements(self, arr: [int]) -> [int]:
        res = [-1]

        for i in range(len(arr)-1,0,-1):
            res.append(max(res[-1], arr[i]))

        return res[::-1]

s = Solution()
print(s.replaceElements([17,18,5,4,6,1]))