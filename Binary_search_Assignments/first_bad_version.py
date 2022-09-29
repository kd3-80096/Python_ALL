first_bad = 0   ## isBadVersion is already given to us
def isBadVersion(version):
   if version >= first_bad:
      return True
   return False

### Solution###

class Solution:
   def firstBadVersion(self, n):
      l = 1
      r = n

      while l <= r:
         mid = (l + r) // 2
         if isBadVersion(mid):
            if mid - 1 >= 1 and isBadVersion(mid - 1):
               r = mid - 1
               continue
            return mid
         else:
            l = mid + 1




ob1 = Solution()
first_bad = 4  ## At 4th position the first bad program is there
op = ob1.firstBadVersion(9)
print(op)


