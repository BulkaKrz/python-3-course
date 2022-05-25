def generate_infinity_multiplication():
    number = 0
    while True:
        print("Start number = ",number)
        # number = number + 1
        number = yield number * number
        print("po yeld number = ",number)


generatedNumbers = []
numberGenerator = generate_infinity_multiplication()
numberGenerator.send(None)       # możemy teżnapisać next(numberGenerator) - żeby zainicjować działnie generatora




for i in range(10):
    generatedNumbers.append(numberGenerator.send(i))
    

print(generatedNumbers)

generatedNumbers.clear()


for i in range(30, 40):
    generatedNumbers.append(numberGenerator.send(i))

print(generatedNumbers)

