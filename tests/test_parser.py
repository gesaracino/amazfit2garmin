from amazfit2garmin.mapper import GarminSport
from amazfit2garmin.parser import parse_csv, to_float, to_int

CSV_HEADER = (
    "type,startTime,sportTime(s),maxPace(/meter),"
    "minPace(/meter),distance(m),avgPace(/meter),calories(kcal)\n"
)


def test_parse_single_running_activity(tmp_path):

    csv_file = tmp_path / "SPORT.csv"

    csv_file.write_text(
        CSV_HEADER
        + "1,2026-06-19 04:43:15+0000,2539,0.0,0.25922883,7534.0,0.335,526.0\n",
        encoding="utf-8",
    )

    activities = parse_csv(csv_file)

    assert len(activities) == 1

    activity = activities[0]

    assert activity.zepp_sport_type == 1
    assert activity.zepp_sport_name == "Outdoor Running"
    assert activity.garmin_sport == GarminSport.RUNNING
    assert activity.duration_seconds == 2539
    assert activity.distance_meters == 7534.0
    assert activity.calories_kcal == 526.0


def test_parse_multiple_activities(tmp_path):

    csv_file = tmp_path / "SPORT.csv"

    csv_file.write_text(
        CSV_HEADER
        + "1,2026-06-19 04:43:15+0000,2539,0.0,0.25922883,7534.0,0.335,526.0\n"
        + "16,2026-06-18 05:19:55+0000,2076,0.0,0.22833364,591.0,3.508,240.0\n",
        encoding="utf-8",
    )

    activities = parse_csv(csv_file)

    assert len(activities) == 2

    assert activities[0].garmin_sport == GarminSport.RUNNING
    assert activities[1].garmin_sport == GarminSport.OTHER


def test_parser_skips_invalid_rows(tmp_path):

    csv_file = tmp_path / "SPORT.csv"

    csv_file.write_text(
        CSV_HEADER
        + "INVALID LINE\n"
        + "1,2026-06-19 04:43:15+0000,2539,0.0,0.25922883,7534.0,0.335,526.0\n",
        encoding="utf-8",
    )

    activities = parse_csv(csv_file)

    assert len(activities) == 1


def test_unknown_sport_is_imported(tmp_path):

    csv_file = tmp_path / "SPORT.csv"

    csv_file.write_text(
        CSV_HEADER
        + "999,2026-06-19 04:43:15+0000,2539,0.0,0.25922883,100.0,1.0,100.0\n",
        encoding="utf-8",
    )

    activities = parse_csv(csv_file)

    assert len(activities) == 1

    activity = activities[0]

    assert activity.zepp_sport_name == "Unknown"
    assert activity.garmin_sport == GarminSport.OTHER


def test_parser_supports_utf8_bom(tmp_path):

    csv_file = tmp_path / "SPORT.csv"

    csv_file.write_text(
        "\ufeff"
        + CSV_HEADER
        + "1,2026-06-19 04:43:15+0000,2539,0.0,0.25922883,7534.0,0.335,526.0\n",
        encoding="utf-8",
    )

    activities = parse_csv(csv_file)

    assert len(activities) == 1


def test_to_int():

    assert to_int("42") == 42


def test_to_float():

    assert to_float("3.14") == 3.14


def test_to_float_empty_returns_none():

    assert to_float("") is None


def test_to_float_strips_spaces():

    assert to_float("   2.5   ") == 2.5