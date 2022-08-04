mylist = ["Bob", "Tom", "Rick"]
# cant modify tuples
mytuple = ("Bob", "Tom", "Rick")
# cant duplicate elements in set and they are not organized
myset = {"Bob", "Tom", "Rick"}

print(mylist[0])

mylist[0] = "John"
mylist.append("smith")
mylist.remove("Tom")
myset.add("Harvey")

print(mylist, myset)