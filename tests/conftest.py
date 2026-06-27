from datetime import datetime, timezone

import pytest

from amazfit2garmin.activity import Activity
from amazfit2garmin.mapper import GarminSport


@pytest.fixture
def running_activity():

    return Activity(
        zepp_sport_type=1,
        zepp_sport_name="Outdoor Running",
        garmin_sport=GarminSport.RUNNING,
        start_time=datetime(
            2026,
            6,
            19,
            4,
            43,
            15,
            tzinfo=timezone.utc,
        ),
        duration_seconds=2539,
        distance_meters=7534.0,
        calories_kcal=526,
        avg_pace=0.335,
        min_pace=0.259,
        max_pace=0.0,
    )


@pytest.fixture
def bodyweight_activity():

    return Activity(
        zepp_sport_type=16,
        zepp_sport_name="Bodyweight Training",
        garmin_sport=GarminSport.OTHER,
        start_time=datetime(
            2026,
            6,
            18,
            5,
            19,
            55,
            tzinfo=timezone.utc,
        ),
        duration_seconds=2076,
        distance_meters=591.0,
        calories_kcal=240,
        avg_pace=3.508,
        min_pace=0.228,
        max_pace=0.0,
    )