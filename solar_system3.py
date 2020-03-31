import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as an
from scipy.integrate import solve_ivp
import solar_system_data_2
import spaceship

# animation constants
FPS = 25
SUN_NORMAL_FACTOR = 50
PLANETS_NORMAL_FACTOR = 5e2
GIF_NAME = r'solar_system_1.mp4'

# physical constants
G = 6.674e-11  # m**3/(kg*s**2) - gravity constant
SOLAR_SYSTEM = solar_system_data_2.solar_system_dict()
SOLAR_SYSTEM_ORDER = solar_system_data_2.SOLAR_SYSTEM_ORDER
SOLAR_SYSTEM_SIZE = solar_system_data_2.SOLAR_SYSTEM_SIZE
DATE = solar_system_data_2.DATE
LAUNCH_DATE = {"day": 17, "month": 7, "year": 2020}
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# constants of numerical scheme
NUMERICAL_METHOD = "RK45"
ACCURACY = 1e-15
STARTING_TIME = 0  # s
END_TIME = 4 * SOLAR_SYSTEM["earth"].get_year()  # s (multiple of 4 years for accuracy)
DT = 24*60*60  # s

# spaceship global
ship = None
pause = False


def plot_graph(vals, xlabel, ylabel, haedline):
    """
    the function plots a graph.
    :param x: a list of the x axis data.
    :param y: a list of the y axis data.
    :param xlabel: the x axis label.
    :param ylabel: the y axis label.
    :param haedline: the headline of the graph.
    :return: None.
    """
    plt.figure()
    for x, y in vals:
        plt.plot(x, y)
    plt.title(haedline)
    plt.xlabel(xlabel, size=15)
    plt.ylabel(ylabel, size=15)
    plt.grid()
    plt.show()


def calc_stars_theta_dot(t, y):
    """
    calc the next stars location.
    :param t: the current time.
    :param y: the stars location.
    :return: the next stars location.
    """
    new_y = []
    for index, planet in enumerate(SOLAR_SYSTEM_ORDER):
        new_y.append(calc_theta_dot(y[index], SOLAR_SYSTEM[planet].get_angular_momentum(),
                     SOLAR_SYSTEM[planet].get_mass(), SOLAR_SYSTEM[planet].get_eccentricity(),
                     SOLAR_SYSTEM[planet].get_mean_radius()))
    return new_y


def calc_theta_dot(theta, L, m, epsilon, mean_r):
    """
    the function calc the star theta dot.
    :param theta: the star theta.
    :param L: the star's angle momentum.
    :param m: the star's mass.
    :param epsilon: the eccentricity of the star.
    :param mean_r: the mean radius of the star.
    :return: the star theta dot.
    """
    return (L / m) * (1 - epsilon * np.cos(theta))**2 / mean_r**2


def animation(planets_locations_by_time):
    fig, ax = plt.subplots()
    ax.set_xlim([-SOLAR_SYSTEM_SIZE, SOLAR_SYSTEM_SIZE])
    ax.set_ylim([-SOLAR_SYSTEM_SIZE, SOLAR_SYSTEM_SIZE])
    sun = plt.Circle(SOLAR_SYSTEM["sun"].get_location(),
                     SOLAR_SYSTEM["sun"].get_radius()*SUN_NORMAL_FACTOR,
                     color=SOLAR_SYSTEM["sun"].get_color())
    artists = []
    ax.add_artist(sun)
    for planet in SOLAR_SYSTEM_ORDER:
        artists.append(ax.add_artist(plt.Circle(SOLAR_SYSTEM[planet].get_location(),
                       SOLAR_SYSTEM[planet].get_radius()*PLANETS_NORMAL_FACTOR,
                       color=SOLAR_SYSTEM[planet].get_color())))
    anim = FuncAnimation(fig, lambda i: update(i, ax, artists, planets_locations_by_time),
                         frames=int((END_TIME - STARTING_TIME)/DT), interval=1000/FPS)
    plt.show()
    # anim.save(GIF_NAME, dpi=80, writer='ffmpeg')
    # w = an.writers['FFmpeg']
    # writer = w(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # writer = an.FFMpegFileWriter(fps=25, metadata=dict(artist='bww'), bitrate=1800)
    # anim.save(GIF_NAME, writer=writer)


def update(i, ax, artists, planets_locations_by_time):
    global ship, pause
    if not pause:
        update_date()
        label = f"date: {DATE['day']}.{DATE['month']}.{DATE['year']}"
        ax.set_title(label)
        if DATE["year"] == LAUNCH_DATE["year"] and \
           DATE["month"] == LAUNCH_DATE["month"] and \
           DATE["day"] == LAUNCH_DATE["day"]:
            earth_location = planets_locations_by_time[SOLAR_SYSTEM_ORDER.index("earth")]
            earth_velocity = calc_velocity(i, earth_location[0], earth_location[1])
            ship = spaceship.get_spaceship([earth_location[0][i], earth_location[1][i]], [earth_velocity + 3576, 0])
            artists.append(plt.plot([], [], 'o')[0])
            ship_course = ship.get_course()
            artists[-1].set_data(ship_course[0], ship_course[1])
        elif ship:
            mars_location = planets_locations_by_time[SOLAR_SYSTEM_ORDER.index("mars")]
            ship.calc_direction(mars_location[0][i], mars_location[1][i])
            ship.move_spaceship(DT)
            ship_course = ship.get_course()
            artists[-1].set_data(ship_course[0], ship_course[1])
            print(ship.calc_distance(mars_location[0][i], mars_location[1][i]))
            if ship.is_arrived(mars_location[0][i], mars_location[1][i]):
                pause = True
        for index, planet in enumerate(SOLAR_SYSTEM_ORDER):
            artists[index].center = planets_locations_by_time[index][0][i],\
                                    planets_locations_by_time[index][1][i]
    return tuple(artists + [ax])


def calc_velocity(i, x, y):
    if i == 0 or i == len(x) - 1:
        return None
    v1 = np.sqrt(((x[i] - x[i-1])/DT)**2 + ((y[i] - y[i-1])/DT)**2)
    v2 = np.sqrt(((x[i+1] - x[i])/DT)**2 + ((y[i+1] - y[i])/DT)**2)
    return (v1 + v2)/2


def update_date():
    if DATE["year"] % 4 == 0 and DATE["month"] == 2:
        add = 1
    else:
        add = 0
    if DATE["day"] < MONTH_DAYS[DATE["month"] - 1] + add:
        DATE["day"] += 1
    else:
        DATE["day"] = 1
        if DATE["month"] == 12:
            DATE["month"] = 1
            DATE["year"] += 1
        else:
            DATE["month"] += 1


def main():
    """
    the main function of the simulation.
    :return: None.
    """
    time = np.linspace(start=STARTING_TIME, stop=END_TIME, num=int((END_TIME - STARTING_TIME)/DT))
    sol = solve_ivp(fun=calc_stars_theta_dot, t_span=[STARTING_TIME, END_TIME], t_eval=time,
                    y0=[SOLAR_SYSTEM[planet].get_theta() for planet in SOLAR_SYSTEM_ORDER],
                    method=NUMERICAL_METHOD, rtol=ACCURACY)
    stars_angles = sol.y
    planets_location_by_time = []
    for index, planet in enumerate(SOLAR_SYSTEM_ORDER):
        planet_theta_arr = stars_angles[index]
        planet_radius_arr = SOLAR_SYSTEM[planet].get_mean_radius() / (1 - SOLAR_SYSTEM[planet].get_eccentricity() *
                                                                      np.cos(planet_theta_arr))
        planet_x_arr = planet_radius_arr * np.cos(planet_theta_arr)
        planet_y_arr = planet_radius_arr * np.sin(planet_theta_arr)
        planets_location_by_time.append((planet_x_arr, planet_y_arr))
    plot_graph(planets_location_by_time, "x", "y", "solar system")
    animation(planets_location_by_time)
    sol_ship = solve_ivp(fun=calc_stars_theta_dot, t_span=[STARTING_TIME, END_TIME], t_eval=time,
                         y0=[],
                         method=NUMERICAL_METHOD, rtol=ACCURACY)


if __name__ == "__main__":
    main()
