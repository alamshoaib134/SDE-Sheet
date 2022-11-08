class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = nums1[:m]
        i = 0
        j = 0
        a =[]
        while i<m and j<n:
          if nums1[i]>nums2[0]:

              nums1[i],nums2[0] = nums2[0],nums1[i]
              for x in range(len(nums2)-1):
                  if nums2[x] > nums2[x+1]:
                      nums2[x],nums2[x+1] = nums2[x+1],nums2[x]
          i+=1
        for x in range(n):
            nums1[i] = nums2[x]
            i+=1


        
        