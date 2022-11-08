class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(len(nums)-1)):
            if nums[i]<nums[i+1]:
                break
        else:
                nums.reverse()
                return
        if len(nums)>1:
            j = next(j for j in reversed(range(i+1,len(nums))) if nums[i]<nums[j])
            nums[i],nums[j] = nums[j],nums[i]
            nums[i+1:] = reversed(nums[i+1:])
            return

            
        