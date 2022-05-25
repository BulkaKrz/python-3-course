"""
import sys
evenNumbers = [element
               for element in range (400)
               if (element %2 == 0)
               ]

evenNumbersGenerator = (element
                        for element in range(101)
                        
                        )


#print("--evenNumbers----")
#print(sys.getsizeof(evenNumbers))
#print("---evenNumbersGenerato---")
#print(sys.getsizeof(evenNumbersGenerator))


for item in evenNumbersGenerator:
    print(item)
    
print(sum(evenNumbersGenerator))

"""
names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

namesLenght = {
    name : len(name)
    for name in names
    if name.startswith("A")
}

multipliedNumbers = {
    number : number*number
    for number in numbers
    }

sqrNumbers = {
    number : number ** 2
    for number in numbers

}

farenheit = {
    key : celcius * 1.8 +32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20

}


