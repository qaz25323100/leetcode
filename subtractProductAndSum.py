class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_result = 1
        sum_result = 0
        
        for i in str(n):
            product_result *= int(i)
            sum_result += int(i)

        return product_result-sum_result

s = Solution()
print(s.subtractProductAndSum(234))