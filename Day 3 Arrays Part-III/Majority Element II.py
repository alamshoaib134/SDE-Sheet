class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = -999
        num2 = -999
        cnt1 = 0
        cnt2 = 0
        ans = []
        for ele in nums:
            if num1 == ele:
                cnt1+=1
            elif num2 == ele:
                cnt2+=1
            elif cnt1==0:
                num1 = ele
                cnt1 = 1
            elif cnt2 ==0:
                num2 = ele
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        xcnt1 = 0
        xcnt2 = 0
        for ele in nums:
            if ele == num1:
                xcnt1 +=1
            if ele == num2:
                xcnt2 +=1
        if xcnt1 > len(nums)/3:
            ans.append(num1)
        if xcnt2 > len(nums)/3:
            ans.append(num2)
        return ans
            
            
        