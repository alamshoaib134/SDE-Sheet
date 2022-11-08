class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = []
        hashTable = dict()
        flag = 0
        
        for i in range(len(nums)):
            hashTable[nums[i]] = i
            i+=1
        
        for i in range(len(nums)):
            if flag==0:
                compliment = target - nums[i]
                if compliment in hashTable:
                    if i!=hashTable[compliment]:
                        pair.append(i)
                        pair.append(hashTable[compliment])
                        flag = 1
                        return pair
        return pair
            