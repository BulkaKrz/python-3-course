"""
Klasy i obiekty
OOP - Object Oriented Programing
"""


class User():
    """
    This is rocket 
    """
    
    age = 0
    name = ""

    def __init__(self, age, name):
        """_summary_

        Args:
            age (_type_): _description_
            name (_type_): _description_
        """
        print("jestem jakimś tam tekstem")
        self.age = age
        self.name = name

    def print_age(self, message):
        """_summary_

        Args:
            message (_type_): _description_
        """
        print(message, "wiek: ", self.age, self.name)


user1 = User(24, "Arek")
user2 = User(30, "Mirek")


user1.print_age("jakiś dodatkowy tekst wchodzący w zmienną message")


user2.print_age("dodatkowy tekst")
