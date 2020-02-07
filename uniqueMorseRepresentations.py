class Solution:
    def uniqueMorseRepresentations(self, words: [str]) -> int:
        dictionary = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        a = set()

        for i in words:

            tmp = ""
            for j in i:
                tmp += dictionary[ord(j)-97]
            
            a.add(tmp)

        return len(a)
        

s = Solution()
s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])

print(chr(97))