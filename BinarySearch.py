def binary_search(list,first,last,item):
    low=first
    high=last
    while low<=high:
        mid=(low+high)//2
        guess=list[mid]
        if guess == int(item):
            return mid
        elif guess<int(item):
            low=mid+1
        else:
            high=mid-1
    return None
        
    
number=input("Enter a number\n")
mylist=[]
for i in range(1,101) :
    mylist.append(i)
print(binary_search(mylist,0,len(mylist)-1, number))