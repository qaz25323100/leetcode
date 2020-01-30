class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        lcp = ""
        for s in zip(*strs):
            print((s[0],))

s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])