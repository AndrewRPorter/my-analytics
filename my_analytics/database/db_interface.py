import sqlite3
from dataclasses import asdict

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
        place = models.MOZ_PLACE(**data)  # create dataclass
        places.append(place)

    places.sort(key=lambda x: x.visit_count, reverse=True)  # sort based on visit count

    conn.close()

    places = [asdict(place) for place in places]  # convert dataclass to dict

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
        visit = models.MOZ_HISTORYVISIT(**data)  # create dataclass
        visits.append(visit)

    conn.close()

    visits = [asdict(visit) for visit in visits]  # convert dataclass to dict

    df = pd.DataFrame(visits)
    return df
