""" Problem Statement
Input : 2 integers a and n where a>= 2, n >= 1
Output : Find a ^ n
Approach Used : Divide and Conquer
Small Problem : if n == 1
Big Problem : if n >= 1

"""


def DAC_Power(a, n):
  if n == 1:   ## for the small problem where n==1
    return a
  else:     ## for large problem where n>=1
    mid = n//2 # ----- O(1)
    b = DAC_Power(a, mid)  #-------- O(n/2)  ## here we are recursing the method to divide the n values further more
    c = b * b       # ==== O(1)
    # condition to check whether n is even or odd
    if n % 2 == 0: ## If n is even   -----O(1)
      return c
    else:
      return c * a  ## if n is odd   -----O(1)

print(DAC_Power(3,3))



## Time complexity is O(logn)




















