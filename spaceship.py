import numpy as np


class SpaceShip:
    X = 0
    Y = 1

    SPACESHIP_MASS = "?"
    SPACESHIP_FUEL_AMOUNT = "?"
    SPACESHIP_ENGINE_POWER = "?"

    def __init__(self, location, velocity):
        self.__mass = self.SPACESHIP_MASS  # kg
        self.__location = location  # m
        self.__fuel_amount = self.SPACESHIP_FUEL_AMOUNT  # kg
        self.__velocity = velocity  # m / s
        self.__course = ([self.__location[self.X]], [self.__location[self.Y]])  # m

    def get_mass(self):
        return self.__mass

    def get_location(self):
        return self.__location

    def get_fuel_amount(self):
        return self.__fuel_amount

    def get_velocity(self):
        return self.__velocity

    def get_theta(self):
        theta = np.arctan(self.__location[self.Y]/self.__location[self.X])
        if self.__location[self.X] < 0:
            return theta + np.pi
        return theta

    def move_spaceship(self, dt):
        self.__location[self.X] += dt*self.__velocity[0]*np.cos(self.__velocity[1])
        self.__location[self.Y] += dt*self.__velocity[0]*np.sin(self.__velocity[1])
        self.__course[self.X].append(self.__location[self.X])
        self.__course[self.Y].append(self.__location[self.Y])

    def calc_direction(self, x, y):
        theta = np.arctan((y - self.__location[self.Y])/(x - self.__location[self.X]))
        if x - self.__location[self.X] < 0:
            self.__velocity[1] = theta + np.pi
        else:
            self.__velocity[1] = theta

    def get_course(self):
        return self.__course

    def calc_distance(self, x, y):
        return np.sqrt((self.__location[self.X] - x)**2 + (self.__location[self.Y] - y)**2)

    def is_arrived(self, x, y):
        return self.calc_distance(x, y) < 3.5e6


def get_spaceship(location, direction):
    return SpaceShip(location, direction)
