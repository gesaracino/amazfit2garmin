from collections import Counter
from pathlib import Path

from amazfit2garmin.filename import build_filename
from amazfit2garmin.parser import parse_csv
from amazfit2garmin.tcx_writer import TcxWriter


INPUT_FILE = "input/SPORT.csv"
OUTPUT_DIR = Path("output")


def main():
    if not Path(INPUT_FILE).exists():
        print(f"Input file not found: {INPUT_FILE}")
        return
        
    activities = parse_csv(INPUT_FILE)

    activity_counter = Counter(
        activity.garmin_sport.value
        for activity in activities
    )

    writer = TcxWriter()

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    generated = 0

    for index, activity in enumerate(activities, start=1):
        filename = build_filename(
            index,
            activity,
        )

        output_file = OUTPUT_DIR / filename

        writer.write(
            activity,
            output_file,
        )

        generated += 1

    print()

    print("=" * 50)

    print(f"Loaded activities : {len(activities)}")

    print()

    for sport, count in sorted(activity_counter.items()):
        print(f"{sport:<18}: {count}")

    print()

    print(f"Generated files   : {generated}")
    print(f"Output directory  : {OUTPUT_DIR}")

    print("=" * 50)


if __name__ == "__main__":
    main()