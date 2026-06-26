from amazfit2garmin.activity import Activity
from amazfit2garmin.mapper import GarminSport


def get_distance_meters(activity: Activity) -> float:
    """
    Returns the distance that should be exported to Garmin.

    Bodyweight workouts and other non-running activities are exported
    with a distance of 0 meters to avoid affecting Garmin statistics.
    """

    if activity.garmin_sport == GarminSport.RUNNING:
        return activity.distance_meters

    return 0.0


def get_average_speed(activity: Activity) -> float:
    """
    Returns the average speed in meters per second.
    Garmin stores this value inside the MaximumSpeed field when
    no detailed speed samples are available.
    """

    distance = get_distance_meters(activity)

    if activity.duration_seconds <= 0:
        return 0.0

    return distance / activity.duration_seconds