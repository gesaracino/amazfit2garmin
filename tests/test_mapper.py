from amazfit2garmin.mapper import (
    GarminSport,
    get_garmin_sport,
    get_sport_name,
)


def test_running_sport_name():

    assert get_sport_name(1) == "Outdoor Running"


def test_bodyweight_sport_name():

    assert get_sport_name(16) == "Bodyweight Training"


def test_unknown_sport_name():

    assert get_sport_name(999) == "Unknown"


def test_running_mapping():

    assert get_garmin_sport(1) == GarminSport.RUNNING


def test_bodyweight_mapping():

    assert get_garmin_sport(16) == GarminSport.OTHER


def test_unknown_mapping():

    assert get_garmin_sport(999) == GarminSport.OTHER