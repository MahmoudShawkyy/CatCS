def binary_search(list ,low,high,item):
      if low<=high:
            mid=(high+low)//2
            if list[mid]==int(item):
                  return mid
            elif list[mid]>item:
                  return binary_search(list,low,mid-1,item)
            else:
                  return binary_search(list,mid+1,high,item)
      else:
            return None
mylist=[1,2,3,4,5,6,7,8,9,10]
num=int(input("Enter a number between 1 and 10\n"))
print(binary_search(mylist,0,len(mylist)-1,num))