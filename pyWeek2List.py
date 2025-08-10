# list operations

# 1: create an empty list
myList = []
print(myList, f" : My List Before Append")

# 2: Append elements 10, 20, 30, 40 to the list
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
print(myList, f" : My List After Append")

# 3: Insert the value 15 at the second position
myList.insert(1, 15)
print(myList, f" : My List After Inserting 15")

# 4: Extend the list with another list [50, 60, 70]
mySecondList = [50, 60, 70]
myList.extend(mySecondList)
print(myList, f" : My List After Extending")

# 5: Remove the last element from the list
myList.pop()
print(myList, f" : My List Ater Removing the last")

# 6: Sort the list in ascending order
myList.sort()
print(myList, f" : My List After Sorting")

# 7: Find and print the index of the value 30
index_of_30 = myList.index(30)
print("Index of 30:", index_of_30)