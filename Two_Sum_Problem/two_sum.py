""" Addition of two of the elements in the array is equal to one of element in two sum """


def two_sum(arr:list[int],target:int)->list[int]:
    dict ={}

    for idx,value in enumerate(arr):
        required_num = target-arr[idx]

        if required_num in dict:
            return [idx,dict[required_num]]

        else:
            dict[value]=idx

    return 1


arr = [2,1,5,3]
target = 4

print(two_sum(arr,target))
