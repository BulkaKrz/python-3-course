try:
    file = open("test.txt","w")
    file.write("sample\n")
    file.write("sample2")

finally:
    file.close()
