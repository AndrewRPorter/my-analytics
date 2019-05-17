import random

import numpy as np
from matplotlib import dates as mdates
from matplotlib import pyplot as plt
from pytz import timezone

from my_analytics.database import db_interface

tz = timezone("US/Eastern")  # setting EST timezone information
plt.style.use("ggplot")


def plot_all():
    places = db_interface.get_all_places()
    visits = db_interface.get_all_visits()

    fig, ax = plt.subplots()

    places = places[:15]

    x, y, z = places.url, np.random.rand(len(places.url)), places.visit_count

    for _x, _y, _z in zip(x, y, z):
        plt.scatter(
            _x,
            _y,
            s=25 * _z,
            color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
        )

    # add visit count annotation to plots
    for i, txt in enumerate(x):
        place = places[places.url == txt]  # get current 'place' series
        txt += f" ({int(place.visit_count)})"
        ax.annotate(txt, (x[i], y[i]))

    plt.title("Website Usage Visit Distributions")
    plt.xticks([])  # remove x ticks
    plt.yticks([])  # remove y ticks
    plt.show()
