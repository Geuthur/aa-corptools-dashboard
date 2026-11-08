# Changelog

## [In Development] - Unreleased

<!--
> [!NOTE]
>

> [!TIP]
>

> [!IMPORTANT]
>

> [!WARNING]
>

> [!CAUTION]
>

Section Order:

### Added
### Fixed
### Changed
### Removed
-->

<!-- Your changes go here -->

### Changed

- CI: workflows aligned with the aa-example template: `release.yml` now attaches the build to the GitHub release, `autotester.yml` without Python 3.10
- Dropped Python 3.10 (end of life): `requires-python` is now `>=3.11`, classifier and tox environment removed
- Tests use the shared `AuthTestCase` (and `NoSocketsTestCase`) from `ct_dashboard/tests/__init__.py`, matching the other AA apps; tests no longer access the network
- Add the fixed ESI package metadata `__esi_compatibility_date__` and `__operations__` (`GetStatus`) to `ct_dashboard/__init__.py`

### Removed

- [REMOVED] Own copies of `add_character_to_user`, `add_new_token`, `add_permission_to_user` and the token helpers in `testdata/utils.py` (identical to the ones in `aa-evesde-factory`); `aa-evesde-factory` provides them.

- [REMOVED] `load_allianceauth`, `allianceauth.json`, `create_user_from_evecharacter` and `load_characteraudit` (the fixed-ID loader) in `ct_dashboard/tests/testdata/`; the tests now use `UserMainFactory` (new, in `testdata/factory.py`) and `EveCharacterFactory` from `aa-evesde-factory`.

### Fixed

- Fixed `make coverage` exiting with 0 when tests failed. The reports are still created, and the target now exits with the status of the test run, or with the status of `coverage report` if the tests passed.

## [0.1.0] - 2026-09-10

- pin `allianceauth` dependency to `>=5.2`
- pin `python` dependency to `>=3.10,<3.15`
- Optimized Tests
- Enhance Makefile and configuration management
- Added pre-commit hooks management in pre-commit.mk with commands for installation, uninstallation, updates, and checks.
- Improved Redis command management in redis.mk with better echo messages.
- Updated tests.mk to enhance test running and coverage reporting.
- Modified .pre-commit-config.yaml to use regex for JSON file exclusion.
- Updated CHANGELOG.md to include a section for new changes.
- Enhanced CODE_OF_CONDUCT.md with a structured table of contents.
- Improved CONTRIBUTING.md with a structured table of contents.
- Refactored Makefile to include dynamic configuration loading from .ini files. thanks to (@ppfeufer)
- Added database management tasks in database.mk for backup, restore, list, and delete operations.
- Introduced npm.mk for managing npm dependencies and scripts.

## [0.0.2] - 2026-06-03

### Added

- Compatibility to Alliance Auth v5
- Python 3.13 Support

### Removed

- Compatibility to Alliance Auth v4

## [0.0.1] - 2026-03-26

### Added

- Initial public release

<!-- Links -->

[0.0.1]: https://github.com/Geuthur/aa-corptools-dashboard/compare/v0.0.1...v0.0.1 "v0.0.1"
[0.0.2]: https://github.com/Geuthur/aa-corptools-dashboard/compare/v0.0.1...v0.0.2 "v0.0.2"
[0.1.0]: https://github.com/Geuthur/aa-corptools-dashboard/compare/v0.0.2...v0.1.0 "v0.1.0"
[in development]: https://github.com/Geuthur/aa-corptools-dashboard/compare/v0.0.2...HEAD "In Development"
