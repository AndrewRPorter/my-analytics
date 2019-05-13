from matplotlib import dates as mdates
from matplotlib import pyplot as plt
from pytz import timezone

from my_analytics.database import db_interface

tz = timezone("US/Eastern")  # setting EST timezone information

plt.style.use("ggplot")


def plot_places():
    places = db_interface.get_all_places()
    visits = db_interface.get_all_visits()
    print(visits)

    f, ax = plt.subplots()
    # plt.show()
