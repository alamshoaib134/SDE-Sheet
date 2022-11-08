def binary_search(nums: List[int], low: int, high: int, target: int) -> int:
    if high>=low:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binary_search(nums,low,mid-1,target)
        else:
            return binary_search(nums,mid+1, low , target)
    else:
        return -1
    
def lin_search(nums,k,search):
    for i in range(k,len(nums)):
        if nums[i] == search:
            return i
    return -1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        flag = 0
        for i in range(len(nums)-1):
            search =  target - nums[i]
            if(all(nums[i+1] <= nums[i + 2] for i in range(len(nums)-2))):
                flag = 1
            if flag ==1:
                if binary_search(nums, i+1,len(nums), search) !=-1:
                    res.append(i)
                    res.append(binary_search(nums, i+1,len(nums), search))
                    break
            else:
                x = lin_search(nums,i+1,search)
                if  x!= -1:
                    res.append(i)
                    res.append(x)
                    break
        return res
        