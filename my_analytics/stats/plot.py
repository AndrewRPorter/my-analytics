import random
from datetime import datetime

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from my_analytics.database import db_interface
from my_analytics.stats.colors import ColorEnum

plt.style.use("ggplot")


def plot_visit_counts():
    """Plots a random distribution of place visit counts"""
    places = db_interface.get_all_places()

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


def plot_visit_times():
    """Scatters visit times"""
    visits = db_interface.get_all_visits()
    places = db_interface.get_all_places()
    visits["visit_month"] = visits["visit_date"].apply(
        lambda x: datetime.fromtimestamp(x / 1_000_000).strftime("%B")
    )  # get string representation of month
    visits["visit_hour"] = visits["visit_date"].apply(
        lambda x: int(datetime.fromtimestamp(x / 1_000_000).strftime("%H"))
    )  # get 24 hour value

    visit_counts = []
    for index, row in visits.iterrows():
        place = places[places.id == row.id]
        try:
            visit_counts.append(int(place.visit_count))
        except TypeError:  # some places have no visit_count
            visit_counts.append(0)

    x, y, z = visits.visit_hour, visit_counts, visits.visit_month

    for _x, _y, _z in zip(x, y, z):
        color = ColorEnum[_z].value  # index ColorEnum to get color for specific month
        plt.scatter(_x, _y, s=10 * _y, color=color)

    plt.title("Site Visit Time Distribution")
    plt.ylabel("Visit Count")
    plt.xlabel("Time (HH:MM)")
    plt.xticks(
        range(0, 24),
        (
            "00:00",
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ),
    )  # set 24 hour x axis ticks
    plt.show()
