print("jaką chcesz zrobić działanie?")
wybor = input('Wprowaadź:/n + \t dodawanie \n - \t odejmowanie \n * \t mnożenie \n / \t dzielenie \n :')
a = int(input('wprowadź a : '))
b = int(input('wprowadź b : '))

if wybor == "+":
    print(a,'+',b,'=',a+b)

elif wybor == "-":
    print(a,'-',b,'=',a-b)

elif wybor == "*":
    print(a,'*',b,'=',a*b)

elif wybor == "/":
    if b == 0:
        print("b nie może być zero. Niedzielimy przez zero.")
    else:
        print(a,'/',b,'=',a/b)
else:
    print("nie dokonałeś prawidłowego wyboru")
