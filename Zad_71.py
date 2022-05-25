
with open("oceany.txt", "a+", encoding="UTF-8") as file:
    print(file.tell())
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write("\nOcean Kapitana Sparrowa")
    file.seek(0)
    print(file.read())
    
