from enum import Enum, unique


@unique
class ColorEnum(Enum):
    """Enumerations for unique month colors"""

    January = "lightcoral"
    February = "lightgreen"
    March = "peru"
    April = "olive"
    May = "blueviolet"
    June = "navy"
    July = "indianred"
    August = "fuchsia"
    September = "olivedrab"
    October = "navajowhite"
    November = "mediumblue"
    December = "forestgreen"
