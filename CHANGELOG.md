# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project follows [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Support for Zepp activity type 9 (Biking).

### Changed

### Fixed

## [0.1.0] - 2026-06-28

### Added

* Initial public release.
* Support for parsing Zepp `SPORT.csv` exports.
* Conversion of activities to Garmin-compatible TCX files.
* Preservation of historical workout history when migrating from Zepp to Garmin Connect.
* Support for the following activity types:

  * Running
  * Bodyweight Training
* Command-line interface for batch conversion.
* Deterministic output filenames based on activity date and sport.
* Modern Python packaging with `pyproject.toml`.
* Automated test suite using `pytest`.
* Continuous Integration with GitHub Actions.
* Code quality checks with Ruff.
* MIT License.
* Comprehensive project documentation.

### Changed

### Fixed

* Improved compatibility of generated TCX files with Garmin Connect.
* Correct export of activity duration.
* Correct handling of non-distance activities by exporting a distance of `0` meters.
