# amazfit2garmin

![CI](https://github.com/gesaracino/amazfit2garmin/actions/workflows/ci.yml/badge.svg)

Convert Amazfit/Zepp workout exports into Garmin TCX files that can be imported into Garmin Connect.

---

## Why this project?

After using an Amazfit GTS since 2019, I decided to switch to a Garmin Forerunner 265. Like many users changing ecosystems, I wanted to preserve years of workout history instead of starting from scratch.

Although the Zepp app allows exporting workout data as CSV files, Garmin Connect does not provide a way to import those exports directly.

This project bridges that gap by converting the exported SPORT.csv file into Garmin-compatible TCX files. Each workout is converted into an individual TCX file that can be imported into Garmin Connect while preserving the most important information, such as the activity date, duration, calories and activity type.

The project was initially developed for my own migration, but it is designed to help anyone moving from the Amazfit/Zepp ecosystem to Garmin.

---

## Features

- Convert Zepp `SPORT.csv` exports to Garmin TCX
- Generate one TCX file for each activity
- Preserve:
  - activity date and time
  - duration
  - calories
  - activity type
- Deterministic file naming
- No external runtime dependencies
- Compatible with Garmin Connect

---

## Supported activity types

| Zepp | Garmin |
|------:|---------|
| 1 | Running |
| 9 | Biking |
| 16 | Other (Bodyweight Workout) |

Additional activity mappings will be added in future releases.

---

## Requirements

- Python 3.11 or newer

---

## Installation

Clone the repository:

```bash
git clone https://github.com/gesaracino/amazfit2garmin.git

cd amazfit2garmin
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

macOS / Linux

```bash
source .venv/bin/activate
```

Install the project:

```bash
pip install -e .
```

The `amazfit2garmin` command will then be available in the active virtual environment.

---

## Usage

Run the converter:

```bash
amazfit2garmin input/SPORT.csv output/
```

where:

- `input/SPORT.csv` is the Zepp export file.
- `output/` is the directory where the generated TCX files will be written.

---

## Input

Export your workout history from the Zepp application.

The converter currently expects the exported file:

```
SPORT.csv
```

with the following columns:

```csv
type,startTime,sportTime(s),maxPace(/meter),minPace(/meter),distance(m),avgPace(/meter),calories(kcal)
```

---

## Output

One TCX file is generated for every activity.

Example:

```
000001_2026-06-25_05-12-50_other.tcx
000002_2026-06-23_04-34-56_running.tcx
...
```

These files can be imported into Garmin Connect.

---

## Tested with

### Source

- Amazfit GTS
- Zepp export

### Destination

- Garmin Connect
- Garmin Forerunner 265

---

## Roadmap

### Completed

- [x] Parse Zepp `SPORT.csv` exports
- [x] Generate Garmin-compatible TCX files
- [x] Preserve workout date, duration and calories
- [x] Export running distance
- [x] Export non-distance activities with zero distance
- [x] Generate Garmin-compatible filenames
- [x] Command-line interface (CLI)
- [x] Automated test suite with `pytest`
- [x] Code linting with `ruff`
- [x] GitHub Actions continuous integration
- [x] Test coverage reporting (`pytest-cov`)

### Planned

- [ ] Export GPS track data (if available)
- [ ] Support additional activity metrics
- [ ] Support additional Zepp sport types
- [ ] Publish package on PyPI

---

## Contributing

Contributions, suggestions and bug reports are welcome.

Please open an Issue before submitting large changes.

---

## License

MIT License

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for the complete release history.