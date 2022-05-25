import time

def function_performance(func, how_many_times = 1, **arg):
    sum = 0
    print(arg.get("what_value"))
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setContainer = {i for i in range(100)}
listContainer = [i for i in range(100)]

def setContainer_searcher(what_value):
    if what_value in setContainer:
        return True
    else:
        return False

def listContainer_searcher(what_value):
    if what_value in listContainer:
        return True
    else:
        return False

def is_element_in(what_value,containier):
    if what_value in containier:
        return True
    else:
        return False

print(function_performance(is_element_in,  500000, what_value=5,containier=setContainer))
print(function_performance(is_element_in,  500000, what_value=5,containier=setContainer))

#print(function_performance(setContainer_searcher, 1, how_many_times = 500000))
#print(function_performance(listContainer_searcher, 1, how_many_times = 500000))
