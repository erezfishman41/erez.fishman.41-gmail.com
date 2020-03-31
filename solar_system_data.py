import numpy as np

# constants od solar system:
SOLAR_SYSTEM_ORDER = ["mercury", "venus", "earth", "mars",
                      "jupyter", "saturn", "uranus", "neptune"]
SOLAR_SYSTEM_SIZE = 4.6e12  # m

# constants of mercury:
MERCURY_RADIUS = 2439000  # m
MERCURY_YEAR = 7600530.24  # s
MERCURY_MASS = 3.302e23  # kg
MERCURY_ECCENTRICITY = 0.20563  # no dimensions
MERCURY_ANGULAR_MOMENTUM = 9.19e38  # kg*m**2/s
MERCURY_MEAN_RADIUS = 56424375744  # m
MERCURY_START_LOCATION = (1, 1)  # m
MERCURY_COLOR = "green"

# constants of venus:
VENUS_RADIUS = 6502000  # m
VENUS_YEAR = 19414139.62  # s
VENUS_MASS = 4.8685e24  # kg
VENUS_ECCENTRICITY = 0.00677323  # no dimensions
VENUS_ANGULAR_MOMENTUM = 1.84e40  # kg*m**2/s
VENUS_MEAN_RADIUS = 1.08004e11  # m
VENUS_START_LOCATION = (1, 1)  # m
VENUS_COLOR = "orange"

# constants of earth:
EARTH_RADIUS = 6372.797e3  # m
EARTH_YEAR = 365.256366*24*60*60  # s
EARTH_MASS = 5.9742e24  # kg
EARTH_ECCENTRICITY = 0.016710219  # no dimensions
EARTH_ANGULAR_MOMENTUM = 2.66e40  # kg*m**2/s
EARTH_MEAN_RADIUS = 1.49485e11  # m
EARTH_START_LOCATION = (1, 1)  # m
EARTH_COLOR = "blue"

# constants of mars:
MARS_RADIUS = 3396200  # m
MARS_YEAR = 59354294.4  # s
MARS_MASS = 6.4171e23  # kg
MARS_ECCENTRICITY = 0.09341233  # no dimensions
MARS_ANGULAR_MOMENTUM = 3.53e39  # kg*m**2/s
MARS_MEAN_RADIUS = 2.6617e11  # m
MARS_START_LOCATION = (1, 1)  # m
MARS_COLOR = "red"

# constants of jupyter:
JUPYTER_RADIUS = 71492000  # m
JUPYTER_YEAR = 374247820.8  # s
JUPYTER_MASS = 1.899e27  # kg
JUPYTER_ECCENTRICITY = 0.04839266  # no dimensions
JUPYTER_ANGULAR_MOMENTUM = 1.93e43  # kg*m**2/s
JUPYTER_MEAN_RADIUS = 7.77099e11  # m
JUPYTER_START_LOCATION = (1, 1)  # m
JUPYTER_COLOR = "orange"

# constants of saturn:
SATURN_RADIUS = 60268000  # m
SATURN_YEAR = 935913052.8  # s
SATURN_MASS = 5.5684e26  # kg
SATURN_ECCENTRICITY = 0.056  # no dimensions
SATURN_ANGULAR_MOMENTUM = 7.82e42  # kg*m**2/s
SATURN_MEAN_RADIUS = 1.4435e12  # m
SATURN_START_LOCATION = (1, 1)  # m
SATURN_COLOR = "brown"

# constants of uranus:
URANUS_RADIUS = 25559000  # m
URANUS_YEAR = 2661041808  # s
URANUS_MASS = 8.68e25  # kg
URANUS_ECCENTRICITY = 0.04716771  # no dimensions
URANUS_ANGULAR_MOMENTUM = 1.7e42  # kg*m**2/s
URANUS_MEAN_RADIUS = 2.87292e12  # m
URANUS_START_LOCATION = (1, 1)  # m
URANUS_COLOR = "purple"

# constants of neptune:
NEPTUNE_RADIUS = 24786000  # m
NEPTUNE_YEAR = 5200416000  # s
NEPTUNE_MASS = 1.024e26  # kg
NEPTUNE_ECCENTRICITY = 0.00858587  # no dimensions
NEPTUNE_ANGULAR_MOMENTUM = 2.5e42  # kg*m**2/s
NEPTUNE_MEAN_RADIUS = 4.49532e12  # m
NEPTUNE_START_LOCATION = (1, 1)  # m
NEPTUNE_COLOR = "aqua"


class Planet:
    X = 0
    Y = 1

    def __init__(self, name, radius, year, mass, eccentricity,
                 angular_momentum, mean_radius, start_location, color):
        self.__name = name
        self.__radius = radius  # m
        self.__year = year  # s
        self.__mass = mass  # kg
        self.__eccentricity = eccentricity  # no dimensions
        self.__angular_momentum = angular_momentum  # kg*m**2/s
        self.__mean_radius = mean_radius  # m
        self.__location = start_location  # m
        self.__color = color

    def get_name(self):
        return self.__name

    def get_radius(self):
        return self.__radius

    def get_year(self):
        return self.__year

    def get_mass(self):
        return self.__mass

    def get_eccentricity(self):
        return self.__eccentricity

    def get_angular_momentum(self):
        return self.__angular_momentum

    def get_mean_radius(self):
        return self.__mean_radius

    def get_location(self):
        return self.__location

    def get_theta(self):
        theta = np.arctan(self.__location[self.Y] / self.__location[self.X])
        if self.__location[self.X] >= 0:
            return theta
        else:
            return theta + np.pi

    def get_color(self):
        return self.__color


class Sun:
    # constants os the sun:
    SUN_RADIUS = 696342e3  # m
    SUN_MASS = 1.989e30  # kg
    SUN_LOCATION = (0, 0)  # m
    SUN_COLOR = "yellow"

    def __init__(self):
        self.__radius = self.SUN_RADIUS
        self.__mass = self.SUN_MASS
        self.__location = self.SUN_LOCATION
        self.__color = self.SUN_COLOR

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    def get_location(self):
        return self.__location

    def get_color(self):
        return self.__color


def solar_system_dict():
    solar_system = dict()
    solar_system["sun"] = Sun()
    solar_system["mercury"] = Planet("mercury", MERCURY_RADIUS, MERCURY_YEAR, MERCURY_MASS,
                                     MERCURY_ECCENTRICITY, MERCURY_ANGULAR_MOMENTUM,
                                     MERCURY_MEAN_RADIUS, MERCURY_START_LOCATION, MERCURY_COLOR)
    solar_system["venus"] = Planet("venus", VENUS_RADIUS, VENUS_YEAR, VENUS_MASS,
                                   VENUS_ECCENTRICITY, VENUS_ANGULAR_MOMENTUM,
                                   VENUS_MEAN_RADIUS, VENUS_START_LOCATION, VENUS_COLOR)
    solar_system["earth"] = Planet("earth", EARTH_RADIUS, EARTH_YEAR, EARTH_MASS,
                                   EARTH_ECCENTRICITY, EARTH_ANGULAR_MOMENTUM,
                                   EARTH_MEAN_RADIUS, EARTH_START_LOCATION, EARTH_COLOR)
    solar_system["mars"] = Planet("mars", MARS_RADIUS, MARS_YEAR, MARS_MASS,
                                  MARS_ECCENTRICITY, MARS_ANGULAR_MOMENTUM,
                                  MARS_MEAN_RADIUS, MARS_START_LOCATION, MARS_COLOR)
    solar_system["jupyter"] = Planet("jupyter", JUPYTER_RADIUS, JUPYTER_YEAR, JUPYTER_MASS,
                                     JUPYTER_ECCENTRICITY, JUPYTER_ANGULAR_MOMENTUM,
                                     JUPYTER_MEAN_RADIUS, JUPYTER_START_LOCATION, JUPYTER_COLOR)
    solar_system["saturn"] = Planet("saturn", SATURN_RADIUS, SATURN_YEAR, SATURN_MASS,
                                    SATURN_ECCENTRICITY, SATURN_ANGULAR_MOMENTUM,
                                    SATURN_MEAN_RADIUS, SATURN_START_LOCATION, SATURN_COLOR)
    solar_system["uranus"] = Planet("uranus", URANUS_RADIUS, URANUS_YEAR, URANUS_MASS,
                                    URANUS_ECCENTRICITY, URANUS_ANGULAR_MOMENTUM,
                                    URANUS_MEAN_RADIUS, URANUS_START_LOCATION, URANUS_COLOR)
    solar_system["neptune"] = Planet("neptune", NEPTUNE_RADIUS, NEPTUNE_YEAR, NEPTUNE_MASS,
                                     NEPTUNE_ECCENTRICITY, NEPTUNE_ANGULAR_MOMENTUM,
                                     NEPTUNE_MEAN_RADIUS, NEPTUNE_START_LOCATION, NEPTUNE_COLOR)
    return solar_system
