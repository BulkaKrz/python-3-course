errno = 50159747054
name = 'Bob'

print("Hello, %s number error is 0x%xx0 !" % (name,errno)) #%x - wyświetla zapis liczby w HEX
print("Hello, %s number error is %d !" % (name,errno))
print('Hey %(a)s, there is a 0x%(b)x error!' % {"a":name, "b":errno})

print()
print("--------------NEW STYLE------------------")
print("Hello, {} its me".format(name))
print("Hey {name}, there is a 0x{errno} error!" .format(name=name, errno=errno))
print("Hey {a}, there is a 0x{b} error!" .format(a=name, b=errno))
print("Hey {name}, there is a 0x{errno:x} error!" .format(name=name, errno=errno))
print("Hey {a}, there is a 0x{b:x} error!" .format(a=name, b=errno))
print()

print("--------------f - Strings------------------")
print(f'Hello, {name}!')
c=5
d=10
print(f'Five plus ten is {c+d} and not {2*(c+d)}. Hex is {2*(c+d):x}')

