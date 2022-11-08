class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rights = n-1
        ups = m-1
        res = int(factorial(rights+ups)/(factorial(rights)*factorial(ups)))
        return res
        