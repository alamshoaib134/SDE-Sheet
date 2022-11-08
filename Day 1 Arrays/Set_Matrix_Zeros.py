class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros =[]

        for i in range(0,len(a)):
            zero = []
            for j in range(0,len(a[0])):
                if a[i][j] == 0:
                    zero.append([i,j])
            zeros.append(zero)
            zeros = [ele for ele in zeros if ele != []]

        # print(zeros)
        for j in range(0,len(a[0])):
            for zero_lsts in zeros:
                for zero_lst in zero_lsts:
                    a[zero_lst[0]][j] = 0
        for i in range(0, len(a)):
           for zero_lsts in zeros:
                for zero_lst in zero_lsts:
                    a[i][zero_lst[1]] = 0
        # print(a)