list=[26,1,5,3,22,10,8,4,71,12,30,55,74,65]

for i in range(len(list)):
    smallest_index=i
    for j in range(smallest_index+1,len(list)):
         if list[j]<list[smallest_index]:
              smallest_index=j
    list[i],list[smallest_index]=list[smallest_index],list[i]
    
print(list)