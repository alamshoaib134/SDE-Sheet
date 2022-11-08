class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        maxi =0
        for i in range(len(nums)):
            hashmap[i] = nums[i]

        for i  in range(len(nums)):
            if nums[i]-1 not in hashmap.values():
                currentnum = nums[i]
                seq = 1 
                while currentnum+1 in hashmap.values():
                    seq+=1
                    currentnum+=1
                maxi = max(maxi,seq)
        return maxi
        
                