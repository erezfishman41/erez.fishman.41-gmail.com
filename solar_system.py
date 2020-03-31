import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import matplotlib.animation as an
from scipy.integrate import solve_ivp

# animation constants
GIF_NAME = r'solar_system_1.mp4'
SUN_LOCATION = (0, 0)

# physical constants
G = 6.674e-11  # m**3/(kg*s**2) - gravity constant

# starting constants:
EARTH_START_THETA = 0  # rad
MARS_START_THETA = 0  # rad
STARTING_DATE = "?"

# constants of earth:
EARTH_ID = 0
EARTH_RADIUS = 6371e3  # m
EARTH_YEAR = 365.25*24*60*60  # s
EARTH_MASS = 5.972e24  # kg
EARTH_ECCENTRICITY = 0.0167  # no dimensions
EARTH_ANGULAR_MOMENTUM = 2.66e40  # kg*m**2/s
EARTH_MEAN_RADIUS = 1.49523e11  # m

# constants of mars:
MARS_ID = 1
MARS_RADIUS = 3389.5e3  # m
MARS_YEAR = "?"
MARS_MASS = 6.4171e23  # kg
MARS_ECCENTRICITY = 0.0934  # no dimensions
MARS_ANGULAR_MOMENTUM = 3.53e39  # kg*m**2/s
MARS_MEAN_RADIUS = 2.299e11  # m

# constants os the sun:
SUN_ID = 2
SUN_RADIUS = 696342e3  # m
SUN_MASS = 1.989e30  # kg

# constants of numerical scheme
NUMERICAL_METHOD = "RK45"
STARTING_TIME = 0  # s
END_TIME = 10 * EARTH_YEAR  # s
DT = 24*60*60  # s


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
    earth_loc = y[EARTH_ID]
    mars_loc = y[MARS_ID]
    return [calc_theta_dot(earth_loc, EARTH_ANGULAR_MOMENTUM, EARTH_MASS,
                           EARTH_ECCENTRICITY, EARTH_MEAN_RADIUS),
            calc_theta_dot(mars_loc, MARS_ANGULAR_MOMENTUM, MARS_MASS,
                           MARS_ECCENTRICITY, MARS_MEAN_RADIUS)]


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


def animation(earth_x, earth_y, mars_x, mars_y):
    fig, ax = plt.subplots()
    ax.set_xlim([-2.6e11, 2.6e11])
    ax.set_ylim([-2.6e11, 2.6e11])
    sun = plt.Circle((0, 0), SUN_RADIUS*50, color="yellow")
    ax.add_artist(sun)
    earth = ax.add_artist(plt.Circle((0, 0), EARTH_RADIUS*5e2, color="blue"))
    mars = ax.add_artist(plt.Circle((0, 0), MARS_RADIUS*5e2, color="red"))
    anim = FuncAnimation(fig, lambda i: update(i, ax, earth, mars, earth_x, earth_y, mars_x, mars_y),
                         frames=int((END_TIME - STARTING_TIME)/DT), interval=40)
    plt.show()
    #anim.save(GIF_NAME, dpi=80, writer='ffmpeg')
    #w = an.writers['FFmpeg']
    #writer = w(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    #writer = an.FFMpegFileWriter(fps=25, metadata=dict(artist='bww'), bitrate=1800)
    #anim.save(GIF_NAME, writer=writer)


def update(i, ax, earth, mars, earth_x, earth_y, mars_x, mars_y):
    print(i)
    earth.center = earth_x[i], earth_y[i]
    mars.center = mars_x[i], mars_y[i]
    return earth, mars, ax


def main():
    """
    the main function of the simulation.
    :return: None.
    """
    time = np.linspace(start=STARTING_TIME, stop=END_TIME, num=int((END_TIME - STARTING_TIME)/DT))
    sol = solve_ivp(fun=calc_stars_theta_dot, t_span=[STARTING_TIME, END_TIME], t_eval=time,
                    y0=[EARTH_START_THETA, MARS_START_THETA], method=NUMERICAL_METHOD, rtol=1e-15)
    locations = sol.y
    earth_theta_arr = locations[EARTH_ID]
    earth_radius_arr = EARTH_MEAN_RADIUS / (1 - EARTH_ECCENTRICITY * np.cos(earth_theta_arr))
    earth_x_arr = earth_radius_arr*np.cos(earth_theta_arr)
    earth_y_arr = earth_radius_arr * np.sin(earth_theta_arr)

    mars_theta_arr = locations[MARS_ID]
    mars_radius_arr = MARS_MEAN_RADIUS / (1 - MARS_ECCENTRICITY * np.cos(mars_theta_arr))
    mars_x_arr = mars_radius_arr * np.cos(mars_theta_arr)
    mars_y_arr = mars_radius_arr * np.sin(mars_theta_arr)
    plot_graph([(earth_x_arr, earth_y_arr), (mars_x_arr, mars_y_arr)], "x", "y", "solar system")
    animation(earth_x_arr, earth_y_arr, mars_x_arr, mars_y_arr)


if __name__ == "__main__":
    main()
