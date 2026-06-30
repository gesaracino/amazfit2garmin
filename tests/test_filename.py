from dataclasses import replace
from datetime import datetime, timezone

from amazfit2garmin.filename import build_filename


def test_build_filename_for_running_activity(running_activity):

    filename = build_filename(
        1,
        running_activity,
    )

    assert (
        filename
        == "000001_2026-06-19_04-43-15_running.tcx"
    )


def test_build_filename_for_other_activity(bodyweight_activity):

    filename = build_filename(
        25,
        bodyweight_activity,
    )

    assert (
        filename
        == "000025_2026-06-18_05-19-55_other.tcx"
    )


def test_build_filename_zero_padded_index(running_activity):

    activity = replace(
        running_activity,
        start_time=datetime(
            2024,
            1,
            2,
            3,
            4,
            5,
            tzinfo=timezone.utc,
        ),
    )

    filename = build_filename(
        123,
        activity,
    )

    assert filename.startswith("000123_")
    assert filename.endswith("_running.tcx")


def test_build_filename_for_biking_activity(
    biking_activity,
):
    filename = build_filename(
        3,
        biking_activity,
    )

    assert filename.endswith("_biking.tcx")
