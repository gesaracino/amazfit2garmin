from __future__ import annotations

import csv
import logging
from datetime import datetime
from pathlib import Path

from amazfit2garmin.activity import Activity
from amazfit2garmin.mapper import (
    get_garmin_sport,
    get_sport_name,
)

logger = logging.getLogger(__name__)

DATE_FORMAT = "%Y-%m-%d %H:%M:%S%z"

FIELD_TYPE = "type"
FIELD_START_TIME = "startTime"
FIELD_DURATION = "sportTime(s)"
FIELD_MAX_PACE = "maxPace(/meter)"
FIELD_MIN_PACE = "minPace(/meter)"
FIELD_AVG_PACE = "avgPace(/meter)"
FIELD_DISTANCE = "distance(m)"
FIELD_CALORIES = "calories(kcal)"


def to_float(value: str) -> float | None:
    value = value.strip()

    if not value:
        return None

    return float(value)


def to_int(value: str) -> int:
    return int(value.strip())


def parse_csv(path: str | Path) -> list[Activity]:
    """
    Parse a Zepp SPORT.csv export.
    """

    activities: list[Activity] = []

    with open(path, newline="", encoding="utf-8-sig") as csvfile:

        reader = csv.DictReader(csvfile)

        for row_number, row in enumerate(reader, start=2):

            try:

                sport_type = to_int(row[FIELD_TYPE])

                activity = Activity(

                    zepp_sport_type=sport_type,

                    zepp_sport_name=get_sport_name(sport_type),

                    garmin_sport=get_garmin_sport(sport_type),

                    start_time=datetime.strptime(
                        row[FIELD_START_TIME],
                        DATE_FORMAT,
                    ),

                    duration_seconds=to_int(
                        row[FIELD_DURATION]
                    ),

                    max_pace=to_float(
                        row[FIELD_MAX_PACE]
                    ),

                    min_pace=to_float(
                        row[FIELD_MIN_PACE]
                    ),

                    avg_pace=to_float(
                        row[FIELD_AVG_PACE]
                    ),

                    distance_meters=float(
                        row[FIELD_DISTANCE]
                    ),

                    calories_kcal=float(
                        row[FIELD_CALORIES]
                    ),

                )

                activities.append(activity)

            except Exception as exc:

                logger.warning(
                    "Skipping row %d: %s (%s)",
                    row_number,
                    exc,
                    row,
                )

    return activities