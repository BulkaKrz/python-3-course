from user import User

a = User("Arkadiusz")
b = User("Wiola")
c = User("Karol")

users = [User() for _ in range(8)]


print(a.id)
print(b.id)
print(c.id)
print("następny id będzie wynosić: ", User.nextId)

for user in users:
    print(user.id)