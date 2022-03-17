def Quick_Sort(list):
    if len(list)<2:
        return list
    else:
        pivot=list[0]
        low=[i for i in list[1:] if i<=pivot]
        high=[i for i in list[1:] if i>pivot]
    return Quick_Sort(low)+[pivot]+Quick_Sort(high)

mylist=[74,37,6,41,11,65,3,10,4,32,7]
print(Quick_Sort(mylist))