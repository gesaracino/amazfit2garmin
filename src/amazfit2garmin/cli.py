from collections import Counter
from pathlib import Path
import argparse

from amazfit2garmin.filename import build_filename
from amazfit2garmin.parser import parse_csv
from amazfit2garmin.tcx_writer import TcxWriter


def main():

    parser = argparse.ArgumentParser(
        description="Convert Zepp SPORT.csv to Garmin TCX files."
    )

    parser.add_argument(
        "input",
        help="Path to SPORT.csv",
    )

    parser.add_argument(
        "output",
        help="Output directory",
    )

    args = parser.parse_args()

    input_file = Path(args.input)
    output_dir = Path(args.output)

    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        return 1

    activities = parse_csv(input_file)

    counter = Counter(
        activity.garmin_sport.value
        for activity in activities
    )

    writer = TcxWriter()

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    generated = 0

    for index, activity in enumerate(
        activities,
        start=1,
    ):

        filename = build_filename(
            index,
            activity,
        )

        writer.write(
            activity,
            output_dir / filename,
        )

        generated += 1

    print()

    print("=" * 50)

    print(f"Loaded activities : {len(activities)}")

    print()

    for sport, count in sorted(counter.items()):
        print(f"{sport:<18}: {count}")

    print()

    print(f"Generated files   : {generated}")
    print(f"Output directory  : {output_dir}")

    print("=" * 50)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())