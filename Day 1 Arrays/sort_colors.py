class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero =0
        one =0
        two=0
        for i in nums:
            if i == 0:
                zero+=1
            elif i==1:
                one+=1
            else:
                two+=1
        nums.clear()
        for i in range(0,zero):
            nums.append(0)
        for i in range(0,one):
            nums.append(1)
        for i in range(0,two):
            nums.append(2)
        
        # print(nums)