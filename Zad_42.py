"""
podzielne przez 7 nie podzielne przez 5 z zakresu 100 470
"""

numbers = [ number
    for number in range(2,471)
    if (number % 7 == 0)
    if (number % 5 != 0)
    ]


print(numbers)
