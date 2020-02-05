class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        counter = 0

        j = set(J)

        for i in S:
            if i in j:
                counter+=1
        
        return counter

s = Solution()
print(s.numJewelsInStones(J = "aA", S = "aAAbbbb"))
print(s.numJewelsInStones(J = "z", S = "ZZZ"))