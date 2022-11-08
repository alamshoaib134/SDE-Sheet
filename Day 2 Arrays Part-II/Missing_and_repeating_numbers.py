# Problem Statement
# You are given an array of size ‘N’. The elements of the array are in the range from 1 to ‘N’.
# Ideally, the array should contain elements from 1 to ‘N’. But due to some miscalculations, there is a number R in the range [1, N] which appears in the array twice and another number M in the range [1, N] which is missing from the array.
# Your task is to find the missing number (M) and the repeating number (R).

def missingAndRepeating(arr, n):
    # Write your code here
	
	S = (n+1)*n/2
	S_ = sum(arr)
	S2 = n*(n+1)*(2*n+1)/6
	S2_ =0
	for ele in arr:
		S2_ = S2_ + ele*ele
	diff = S-S_
	diff_sq = S2 - S2_
	
	sumdiff = diff_sq / diff
	
	X = int((diff + sumdiff)/2)
	Y = int(X - diff)
	return (X,Y)
