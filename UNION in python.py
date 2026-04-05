#UNION
a={1,2,3}
b={4,5,6}
print("The union is",a.union(b))
a={1,2,3}
b={2,4,5,6}
print("The union is",a.union(b))

#INTERSECTION
a={1,2,3}
b={2,3,4,5}
print("The intersection is using &",a&b)

#DIFFERENCE
a={1,9,8,7}
b={2,1,9,5}
print("The difference is using -",a-b)
print("The difference is using -",b-a)

#SYMMETRIC DIFFERENCE
a={1,9,8,7}
b={2,1,9,5}
print("The  Symmetric difference is using ^",a^b)
print("The  Symmetric difference is using ^",b^a)


