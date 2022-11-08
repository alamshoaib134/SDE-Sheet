class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        end = -999999999
        sum =  0
        for i in range(0,len(nums)):
            sum = sum + nums[i]
            if end < sum:
                end = sum
            if sum < 0:
                sum = 0
        return end
                    