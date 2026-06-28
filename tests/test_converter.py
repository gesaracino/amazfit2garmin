from dataclasses import replace

from amazfit2garmin.converter import (
    get_average_speed,
    get_distance_meters,
)


def test_running_distance_is_preserved(running_activity):

    assert get_distance_meters(running_activity) == 7534.0


def test_bodyweight_distance_is_zero(bodyweight_activity):

    assert get_distance_meters(bodyweight_activity) == 0.0


def test_running_average_speed(running_activity):

    speed = get_average_speed(running_activity)

    assert round(speed, 3) == round(7534 / 2539, 3)


def test_bodyweight_average_speed_is_zero(bodyweight_activity):

    assert get_average_speed(bodyweight_activity) == 0.0


def test_zero_duration_average_speed_is_zero(running_activity):

    activity = replace(
        running_activity,
        duration_seconds=0,
    )

    assert get_average_speed(activity) == 0.0