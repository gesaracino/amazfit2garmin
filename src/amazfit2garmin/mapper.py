from dataclasses import dataclass
from enum import Enum


class GarminSport(str, Enum):
    RUNNING = "Running"
    OTHER = "Other"


@dataclass(frozen=True)
class SportMapping:
    """
    Maps a Zepp sport type to its human-readable name and
    the corresponding Garmin sport.
    """

    name: str
    garmin_sport: GarminSport


SPORT_MAP = {
    1: SportMapping(
        name="Outdoor Running",
        garmin_sport=GarminSport.RUNNING,
    ),
    16: SportMapping(
        name="Bodyweight Training",
        garmin_sport=GarminSport.OTHER,
    ),
}

UNKNOWN_SPORT = SportMapping(
    name="Unknown",
    garmin_sport=GarminSport.OTHER,
)


def get_sport_name(sport_type: int) -> str:
    """
    Returns the human-readable Zepp sport name.
    """

    return SPORT_MAP.get(
        sport_type,
        UNKNOWN_SPORT,
    ).name


def get_garmin_sport(sport_type: int) -> GarminSport:
    """
    Returns the Garmin sport associated with the Zepp sport type.
    """

    return SPORT_MAP.get(
        sport_type,
        UNKNOWN_SPORT,
    ).garmin_sport