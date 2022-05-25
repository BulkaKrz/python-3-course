"""
 to będzie zadanie dotycząca rakiety
"""
from random import randint
from math import sqrt


class Rocket():
    """This is Rocket Class
    """

    def __init__(self, altitude, speed=1):
        self.altitude = 0
        self.altitude = altitude
        self.speed = speed
        self.x = 0

    def moveUp(self):
        """_opisujemy szybkość sasa
        dasdasd_
        """
        self.altitude += self.speed

    def __str__(self):
        return("Rakieta jest aktualnie na wysokości: " + str(self.altitude) +
               " \n jej aktualna prędkość to " + str(self.speed))


class RocketBoard:
    """docstring for ClassName."""

    def __init__(self, amountOfRackets=5):

        self.rocketList = [Rocket(randint(1, 6), randint(10, 30))
                           for _ in range(amountOfRackets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, len(self.rocketList) - 1)
            self.rocketList[rocketIndexToMove].moveUp()

        for rocket in self.rocketList:
            print(rocket)

    def __getitem__(self, key):
        return self.rocketList[key]

    def __setitem__(self, key, value):
        self.rocketList[key].altitude = value

    @staticmethod
    def get_distance(rocket1, rocket2):
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2

        return sqrt(ab+bc)
