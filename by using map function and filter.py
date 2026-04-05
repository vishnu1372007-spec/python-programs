#BY USING MAP FUNCTION
nums=[1,2,3,4,5,6]
print(list(map(lambda x:x*2,nums)))

#BY USING FILTER
nums=[2,3,5,4,8,9,10]
print(list(filter(lambda x:x%2!=0,nums)))
