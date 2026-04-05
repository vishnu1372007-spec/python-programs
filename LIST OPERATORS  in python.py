#LIST OPERATORS


list1=[0,1,2,3,4]
list2=[5,6,2,7,8]
print(list2+list2)  #cancatenation
print(list2*3)      #Repetition
print(list1[3])     #indexing
print(list2[-2])
print(list2[0])
print(list1[ :2])   #slicing
print(list2[0: ])
print(list1[ : ])
print(list2[ : :-1])

item=325            #membership
list1=list(range(1,30))
print(item not in list1)
item=7           
list1=list(range(1,30))
print(item in list1)
