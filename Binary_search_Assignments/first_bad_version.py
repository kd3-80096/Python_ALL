first_bad = 0   ## isBadVersion is already given to us
def isBadVersion(version):
   if version >= first_bad:
      return True
   return False

### Solution###

class Solution:
   def firstBadVersion(self, n):
      if n <2:
         return n
      low = 1
      high = n
      while(low<=high):
         mid = (low+high)//2   ## To find the mid value

         if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid

         elif isBadVersion(mid-1):
            high = mid-1
         else:
            low = mid+1

ob1 = Solution()
first_bad = 4  ## At 4th position the first bad program is there
op = ob1.firstBadVersion(9)
print(op)