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
