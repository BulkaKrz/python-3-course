def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList.clear()

myList = [1, 4, 2, 1, 52, 3]

print(id(myList))
evil_function(myList.copy())
