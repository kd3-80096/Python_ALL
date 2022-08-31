def selection(lst):

 for i in range(len(lst)):
     min_pos =i   ## when i will start from 0 minimum position will be 0,then when i will be 1 then min position will be1 and so on
     for j in range(i,len(lst)):
         if lst[j]<lst[min_pos]:
             min_pos=j   ## whenever we find the new smallest number we will make it new minimum position

     lst[i],lst[min_pos]=lst[min_pos],lst[i] ## swapping of the numbers
     print(lst)  ## printing after every_swapping



lst =[3,8,9,45,1,0,2]
selection(lst)
print(lst)