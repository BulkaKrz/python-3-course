class User:
    nextId = 1  # zmienna klasowa

    def __init__(self, name=""):
        self.name = name
        self.id = User.nextId
        User.nextId += 1
