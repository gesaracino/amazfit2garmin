from amazfit2garmin.tcx_writer import TcxWriter
from tests.utils import find, find_all, parse_tcx


def test_writer_creates_tcx_file(tmp_path, running_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        running_activity,
        output_file,
    )

    assert output_file.exists()


def test_activity_has_running_sport(tmp_path, running_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        running_activity,
        output_file,
    )

    root = parse_tcx(output_file)

    activity = find(
        root,
        "tcx:Activities/tcx:Activity",
    )

    assert activity is not None
    assert activity.attrib["Sport"] == "Running"


def test_lap_contains_duration(tmp_path, running_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        running_activity,
        output_file,
    )

    root = parse_tcx(output_file)

    duration = find(
        root,
        ".//tcx:TotalTimeSeconds",
    )

    assert duration is not None
    assert duration.text == "2539.0"


def test_running_distance_is_written(tmp_path, running_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        running_activity,
        output_file,
    )

    root = parse_tcx(output_file)

    distance = find(
        root,
        ".//tcx:Lap/tcx:DistanceMeters",
    )

    assert distance is not None
    assert distance.text == "7534.0"


def test_bodyweight_distance_is_zero(tmp_path, bodyweight_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        bodyweight_activity,
        output_file,
    )

    root = parse_tcx(output_file)

    distance = find(
        root,
        ".//tcx:Lap/tcx:DistanceMeters",
    )

    assert distance is not None
    assert distance.text == "0.0"


def test_track_contains_two_trackpoints(tmp_path, running_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        running_activity,
        output_file,
    )

    root = parse_tcx(output_file)

    trackpoints = find_all(
        root,
        ".//tcx:Trackpoint",
    )

    assert len(trackpoints) == 2


def test_first_trackpoint_distance_is_zero(tmp_path, running_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        running_activity,
        output_file,
    )

    root = parse_tcx(output_file)

    trackpoints = find_all(
        root,
        ".//tcx:Trackpoint",
    )

    first_distance = find(
        trackpoints[0],
        "tcx:DistanceMeters",
    )

    assert first_distance is not None
    assert first_distance.text == "0.0"


def test_last_trackpoint_distance_matches_activity(tmp_path, running_activity):

    output_file = tmp_path / "activity.tcx"

    TcxWriter().write(
        running_activity,
        output_file,
    )

    root = parse_tcx(output_file)

    trackpoints = find_all(
        root,
        ".//tcx:Trackpoint",
    )

    last_distance = find(
        trackpoints[-1],
        "tcx:DistanceMeters",
    )

    assert last_distance is not None
    assert last_distance.text == "7534.0"