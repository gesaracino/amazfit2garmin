from enum import Enum


class GarminSport(str, Enum):
    RUNNING = "Running"
    OTHER = "Other"


SPORT_MAP = {
    1: ("Outdoor Running", GarminSport.RUNNING),
    16: ("Bodyweight Training", GarminSport.OTHER),
}


def get_sport_name(sport_type: int) -> str:
    return SPORT_MAP.get(sport_type, ("Unknown", GarminSport.OTHER))[0]


def get_garmin_sport(sport_type: int) -> GarminSport:
    return SPORT_MAP.get(sport_type, ("Unknown", GarminSport.OTHER))[1]