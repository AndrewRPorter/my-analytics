import sqlite3
import sys

import pandas as pd
import yaml

from . import models

config = yaml.safe_load(open("config.yml"))


def get_all_places():
    conn = sqlite3.connect(config["config"]["places_destination"])
    c = conn.cursor()
    c.execute("SELECT * FROM moz_places")
    column_names = list(map(lambda x: x[0], c.description))

    places = []

    for row in c.fetchall():
        data = dict(zip(column_names, row))
        place = models.MOZ_PLACE(data)
        places.append(place)

    places.sort(key=lambda x: x.visit_count, reverse=True)  # sort based on visit count

    conn.close()

    places = [place.to_dict() for place in places]

    df = pd.DataFrame(places)
    return df


def get_all_visits():
    conn = sqlite3.connect(config["config"]["places_destination"])
    c = conn.cursor()
    c.execute("SELECT * FROM moz_historyvisits")
    column_names = list(map(lambda x: x[0], c.description))

    visits = []

    for row in c.fetchall():
        data = dict(zip(column_names, row))
        visit = models.MOZ_HISTORYVISIT(data)
        visits.append(visit)

    conn.close()

    visits = [visit.to_dict() for visit in visits]

    df = pd.DataFrame(visits)
    return df
