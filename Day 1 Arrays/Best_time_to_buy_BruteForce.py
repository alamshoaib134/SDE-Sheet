class Solution:
    def maxProfit(self, num: List[int]) -> int:
        max = 0
        for i in range(0, len(num)):
            sum =num[i]
            for j in range(i,len(num)):
                sum = num[j] - num[i]
                if max < sum:
                    max = sum
        return max