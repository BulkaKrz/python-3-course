'''Napisz program który policzy sumę wszystkich liczb od 1 do podanej liczby przez użytkownika
mierzenie wydajności skryptu
'''
import time

def sumuj_do(liczba):
    suma = 0
    for liczba in range(1,liczba+1):
        suma = suma + liczba
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, liczba+1)])
    
def sumuj_do3(liczba):
    return (1+liczba)/2*liczba
    
def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1, liczba+1)))

def sumuj_do5(liczba):
    return sum({liczba for liczba in range(1, liczba+1)})

def finish_timer(start):
    end = time.perf_counter()
    return end-start

def function_performers(func, arg, haw_many_times=1):
    sum = 0
    for i in range(0,haw_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
    return sum
    
def show_mesage(mesage):
    print(mesage)
x=50000
print(function_performers(sumuj_do, x ,25))
print(function_performers(sumuj_do2, x))
print(function_performers(sumuj_do3, x))
print(function_performers(sumuj_do4, x))
print(function_performers(sumuj_do5, x))



"""
x=256
print("pętla for")
start = time.perf_counter()
print(sumuj_do(x))
print(finish_timer(start))

print("\n lista")

start = time.perf_counter()
print(sumuj_do2(x))
print(finish_timer(start))

print("\n wzór")
start = time.perf_counter()
print(sumuj_do3(x))
print(finish_timer(start))

print("\n krotka / tuple")
start = time.perf_counter()
print(sumuj_do4(x))
print(finish_timer(start))

print("\n zbiór")
start = time.perf_counter()
print(sumuj_do5(x))
print(finish_timer(start))
"""
