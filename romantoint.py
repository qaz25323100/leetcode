class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanset = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        tmp = 0
        for i in s[::-1]:
            
            if romanset[i] >= tmp:
                sum += romanset[i]
            else:
                sum -= romanset[i]
            tmp = romanset[i]
        
        return sum
s = Solution()
print(s.romanToInt('VI'))
print(s.romanToInt('IV'))

print(s.romanToInt('IVX'))