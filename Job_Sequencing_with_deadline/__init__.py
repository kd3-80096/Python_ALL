""" **Problem Statement :**
Given an array of jobs where every job has a deadline and associated profit if the job is finished
 before the deadline. Objective is to maximize total profit if only one job can be scheduled at a time."""


def jobscheduling(n,max_job):
    ## we will sort the array in decreasing order with respect to profit
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][2] < arr[j+1][2]: ## because at 3rd index in list the profits are stored
                arr[j],arr[j+1] = arr[j+1],arr[j]  ## swap the elements of list

## To Keep the track of the time_slot

    res = [False] * max_job
    job = ['-1'] * max_job

## putting the jobs according to their dates

    for i in range(n):
        for j in range(min(max_job - 1, arr[i][1]-1),-1,-1): ##arr[i][1] contains the no of days

            if res[j] is False:  ## check if the slot is empty
                res[j] = True
                job [j] = arr [i][0]  ## fill with the jobs according to the date
                break
    print("The jobs will be filled as follows ->",job)








arr = [['J1', 5, 50],
       ['J2', 3, 60],
       ['J3', 2, 70],
       ['J4', 4, 55],
       ['J5', 3, 65],
       ['J6', 2, 75],
       ['J7', 3, 90]]

n = len(arr)
jobscheduling(n, 5)






