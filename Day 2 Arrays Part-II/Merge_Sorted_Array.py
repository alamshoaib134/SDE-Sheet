#Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        a =[]
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                a.append(nums1[i])
                i+=1 
            elif nums1[i] > nums2[j]:
                a.append(nums2[j])
                j+=1 
            else:
                a.append(nums2[j])
                a.append(nums1[i])
                i+=1 
                j+=1 
        if i<m:
            a.extend(nums1[i:m])
        else:
            a.extend(nums2[j:])

        for i in range(len(a)):
            nums1[i] = a[i]