class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[]]

        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                num = factorial(i)//(factorial(j)*factorial(i-j))
                tmp.append(num)
            lst.append(tmp)    
        return lst[1:]