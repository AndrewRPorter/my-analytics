#!/usr/bin/env python3

import os
import shutil
import sys

import yaml

from my_analytics.stats import plot

config = yaml.safe_load(open("config.yml"))


def run():
    """
    Runs analytics on the places data from firefox
    """
    if os.path.exists(config["config"]["places_directory"]):
        # create a copy of places.sqlite as db is locked due to concurrency issues with sqlite
        shutil.copyfile(
            config["config"]["places_directory"], config["config"]["places_destination"]
        )
    else:
        print(f"Unable to find '{config['config']['places_directory']}'")
        sys.exit()

    plot.plot_all()


if __name__ == "__main__":
    run()
