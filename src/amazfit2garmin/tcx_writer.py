from datetime import timedelta, timezone
from pathlib import Path
from xml.etree.ElementTree import Element, ElementTree, SubElement

from amazfit2garmin.activity import Activity
from amazfit2garmin.converter import (
    get_average_speed,
    get_distance_meters,
)


TCX_NAMESPACE = "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"

XSI_NAMESPACE = "http://www.w3.org/2001/XMLSchema-instance"

SCHEMA_LOCATION = (
    "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 "
    "http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd"
)


class TcxWriter:
    """
    Writes Garmin-compatible TCX files.
    """

    def write(
        self,
        activity: Activity,
        output_path: str | Path,
    ) -> None:

        root = Element(
            "TrainingCenterDatabase",
            {
                "xmlns": TCX_NAMESPACE,
                "xmlns:xsi": XSI_NAMESPACE,
                "xsi:schemaLocation": SCHEMA_LOCATION,
            },
        )

        activities = SubElement(root, "Activities")

        activity_xml = SubElement(
            activities,
            "Activity",
            Sport=activity.garmin_sport.value,
        )

        SubElement(
            activity_xml,
            "Id",
        ).text = self._format_datetime(activity.start_time)

        self._create_lap(
            activity_xml,
            activity,
        )

        tree = ElementTree(root)

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        tree.write(
            output_path,
            encoding="utf-8",
            xml_declaration=True,
        )

    def _create_lap(
        self,
        activity_xml,
        activity: Activity,
    ):

        start_time = activity.start_time

        end_time = start_time + timedelta(
            seconds=activity.duration_seconds
        )

        distance = get_distance_meters(activity)

        lap = SubElement(
            activity_xml,
            "Lap",
            StartTime=self._format_datetime(start_time),
        )

        SubElement(
            lap,
            "TotalTimeSeconds",
        ).text = f"{float(activity.duration_seconds):.1f}"

        SubElement(
            lap,
            "DistanceMeters",
        ).text = f"{distance:.1f}"

        SubElement(
            lap,
            "MaximumSpeed",
        ).text = str(get_average_speed(activity))

        SubElement(
            lap,
            "Calories",
        ).text = str(int(activity.calories_kcal))

        SubElement(
            lap,
            "Intensity",
        ).text = "Active"

        SubElement(
            lap,
            "TriggerMethod",
        ).text = "Manual"

        self._create_track(
            lap,
            start_time,
            end_time,
            distance,
        )

    def _create_track(
        self,
        lap,
        start_time,
        end_time,
        distance,
    ):

        track = SubElement(
            lap,
            "Track",
        )

        start_point = SubElement(
            track,
            "Trackpoint",
        )

        SubElement(
            start_point,
            "Time",
        ).text = self._format_datetime(start_time)

        SubElement(
            start_point,
            "DistanceMeters",
        ).text = "0.0"

        end_point = SubElement(
            track,
            "Trackpoint",
        )

        SubElement(
            end_point,
            "Time",
        ).text = self._format_datetime(end_time)

        SubElement(
            end_point,
            "DistanceMeters",
        ).text = f"{distance:.1f}"

    @staticmethod
    def _format_datetime(dt):

        dt = dt.astimezone(timezone.utc)

        return dt.strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        )