#ADD()
firstset={"East","West","North"}
firstset.add("south")
print(firstset)

#REMOVE()
firstset={"East","West","North"}
firstset.remove("West")
print(firstset)

#DISCARD()
firstset={"East","West","North"}
firstset.discard("West")
print(firstset)

#COPY()
firstset={"East","West","North"}
firstset.copy()
print(firstset)

#POP()
firstset={"East","West","North"}
firstset.pop()
print(firstset)

#LENGTH()
firstset={"East","West","North"}
print(len(firstset))

#UPDATING SET
firstset={"East","West"}
secondset={"North","South"}
firstset.update(secondset)
print(firstset)
