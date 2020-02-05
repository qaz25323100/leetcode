
class Solution:
    def defangIPaddr(self, address: str) -> str:

        res = ""

        for s in address:
            if s == '.':
                res = res + "[.]"
            else:
                res += s

        return res
         

address = "1.1.1.1"

s = Solution()
print(s.defangIPaddr(address))