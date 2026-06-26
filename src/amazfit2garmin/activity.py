from dataclasses import dataclass
from datetime import datetime

from amazfit2garmin.mapper import GarminSport


@dataclass(slots=True, frozen=True)
class Activity:
    """
    Represents a single activity exported from Zepp.
    """

    # Original Zepp information
    zepp_sport_type: int
    zepp_sport_name: str

    # Garmin mapping
    garmin_sport: GarminSport

    # Activity data
    start_time: datetime
    duration_seconds: int
    distance_meters: float
    calories_kcal: float

    # Optional metrics
    avg_pace: float | None = None
    min_pace: float | None = None
    max_pace: float | None = None