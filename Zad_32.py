A = {1,4,20,-4,20,15,17,88,3,2}
print(A)
A.add(7)
print(A)
B = (4,5,6,7,2,3,4,7,9,1,2,4,7,8,8,8,8)
print(B)
print(set(B))
C = {2,5,-4,1,5,8,99,}
print("______________________")
print("A\t",A)
print("C\t",C)

print("&\t",A&C)    #jest w zbiorze A i w zbiorze C
print("|\t",A|C)    #jest w zbiorze A lub w Zbiorze C    
print("-\t",A-C)    #jest w zbiorze A i nie jest w zbiorze C
print("^\t",A^C)    #Jest w zbiorze A i w zbiorze C ale bez elementów wspólnych


