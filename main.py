#!/usr/bin/env python3

import datetime
import os
import shutil
import sqlite3
import sys

import yaml

from my_analytics.database import models

config = yaml.safe_load(open("config.yml"))


def run():
    if os.path.exists(config["config"]["places_directory"]):
        # create a copy of places.sqlite as db is locked due to concurrency issues with sqlite
        shutil.copyfile(
            config["config"]["places_directory"], config["config"]["places_destination"]
        )
    else:
        print(f"Unable to find '{config['config']['places_directory']}'")
        sys.exit()

    try:
        conn = sqlite3.connect(config["config"]["places_destination"])
    except sqlite3.OperationalError:
        print("Unable to open database file")
        sys.exit()

    c = conn.cursor()
    c.execute("SELECT * FROM moz_places")
    column_names = list(map(lambda x: x[0], c.description))

    places = []

    for row in c.fetchall():
        data = dict(zip(column_names, row))
        place = models.MOZ_PLACE(data)
        places.append(place)

    c.execute("SELECT * FROM moz_historyvisits")
    column_names = list(map(lambda x: x[0], c.description))

    visits = []

    for row in c.fetchall():
        data = dict(zip(column_names, row))
        visit = models.MOZ_HISTORYVISIT(data)
        visits.append(visit)

    conn.close()

    places.sort(key=lambda x:x.visit_count, reverse=True)  # sort based on visit count


if __name__ == "__main__":
    run()
