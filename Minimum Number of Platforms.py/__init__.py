## Minimum Number of Platforms Required for a Railway/Bus Station using Sorting:

# Returns minimum number
# of platforms required
 

def findplatform(arr,dep,n):
    ## sorting the arrival and departure

    arr.sort()
    dep.sort()

    # plat_needed indicates
    # number of platforms
    # needed at a time

    plat_needed = 1
    result = 1
    i=1
    j=0

    # Similar to merge in
    # merge sort to process
    # all events in sorted order
    while (i<n and j<n):
        # If next event in sorted
        # order is arrival,
        # increment count of
        # platforms needed

        if (arr[i]<=dep[j]):
            plat_needed+=1
            i+=1

        elif(arr[i] > arr[j]):
            plat_needed-=1
            j+=1

        ## update the reult if neded

        if (result < plat_needed):
            result = plat_needed

    return result







# Driver code
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
 
print("Minimum Number of Platforms Required = ",
      findplatform(arr, dep, n))
 