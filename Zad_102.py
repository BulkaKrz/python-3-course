def generate_infinity_multiplication():
    i=1
    while True:
        x=(i*i)
        i+=1
        yield x

numberGenerator = generate_infinity_multiplication()
    

generatedNumbers = []


for _ in range(20):
    generatedNumbers.append(next(numberGenerator))
    

print(generatedNumbers)

for _ in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)


generatedNumbers.clear()

for _ in range(30):
    generatedNumbers.append(next(numberGenerator))

print(generatedNumbers)
