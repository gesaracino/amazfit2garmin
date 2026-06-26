from amazfit2garmin.activity import Activity


def build_filename(
    index: int,
    activity: Activity,
) -> str:
    """
    Builds a deterministic filename for a generated TCX.
    """

    timestamp = activity.start_time.strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    sport = activity.garmin_sport.value.lower()

    return f"{index:06d}_{timestamp}_{sport}.tcx"