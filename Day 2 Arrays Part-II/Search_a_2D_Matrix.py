# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

def binarySearch(arr, l, r, x):
 
        # Check base case
        if r >= l:

            mid = l + (r - l) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif arr[mid] > x:
                return binarySearch(arr, l, mid-1, x)

            # Else the element can only be present
            # in right subarray
            else:
                return binarySearch(arr, mid + 1, r, x)

        else:
            # Element is not present in the array
            return -1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])


        for ele in matrix:
            # print(ele[col-1])
            if target <= ele[col-1]:

                if(binarySearch(ele,0,len(ele)-1, target) != -1):
                    return True
                else:
                    return False