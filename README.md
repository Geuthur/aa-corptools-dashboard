# Corptools Dashboard Addon module for AllianceAuth.<a name="aa-corptools-dashboard"></a>

![Release](https://img.shields.io/pypi/v/aa-corptools-dashboard?label=release)
![Licence](https://img.shields.io/github/license/geuthur/aa-corptools-dashboard)
![Python](https://img.shields.io/pypi/pyversions/aa-corptools-dashboard)
![Django](https://img.shields.io/pypi/frameworkversions/django/aa-corptools-dashboard.svg?label=django)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Geuthur/aa-corptools-dashboard/master.svg)](https://results.pre-commit.ci/latest/github/Geuthur/aa-corptools-dashboard/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checks](https://github.com/Geuthur/aa-corptools-dashboard/actions/workflows/autotester.yml/badge.svg)](https://github.com/Geuthur/aa-corptools-dashboard/actions/workflows/autotester.yml)
[![codecov](https://codecov.io/gh/Geuthur/aa-corptools-dashboard/graph/badge.svg?token=B3BSovXASa)](https://codecov.io/gh/Geuthur/aa-corptools-dashboard)
[![Translation status](https://weblate.voices-of-war.de/widget/allianceauth/aa-corptools-dashboard/svg-badge.svg)](https://weblate.voices-of-war.de/engage/allianceauth/)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/W7W810Q5J4)

Simple Dashboard Corptools Addon to display not registred Chars

## -

- [AA Corptools Dashboard](#aa-corptools-dashboard)
  - [Features](#features)
  - [Upcoming](#upcoming)
  - [Installation](#features)
    - [Step 1 - Install the Package](#step1)
    - [Step 2 - Configure Alliance Auth](#step2)
    - [Step 3 - Migration to AA](#step3)
  - [Highlights](#highlights)
  - [Translations](#translations)

## Introduce

Everyone knows the issue that some people not register correctly now the members see on the Dashboard that something is wrong...

## Features<a name="features"></a>

- Show not registred Characters on Dashboard
- Corp Tools Character Issue Checker

## Upcoming<a name="upcoming"></a>

- More Information in Dashboard

## Installation<a name="installation"></a>

> [!NOTE]
> AA Corptools Dashboard needs at least Alliance Auth v4.12
> Please make sure to update your Alliance Auth before you install this APP

### Step 1 - Install the Package<a name="step1"></a>

Make sure you're in your virtual environment (venv) of your Alliance Auth then install the pakage.

```shell
pip install aa-corptools-dashboard
```

### Step 2 - Configure Alliance Auth<a name="step2"></a>

Configure your Alliance Auth settings (`local.py`) as follows:

- Add `'corptools',` to `INSTALLED_APPS`
- Add `'ct_dashboard',` to `INSTALLED_APPS`

### Step 3 - Migration to AA<a name="step3"></a>

```shell
python manage.py collectstatic
python manage.py migrate
```

## Highlights<a name="highlights"></a>

## Translations<a name="translations"></a>

[![Translations](https://weblate.voices-of-war.de/widget/allianceauth/aa-corptools-dashboard/multi-auto.svg)](https://weblate.voices-of-war.de/engage/allianceauth/)

Help us translate this app into your language or improve existing translations. Join our team!"

## Contributing <a name="contributing"></a>

You want to improve the project?
Please ensure you read the [contribution guidelines](https://github.com/Geuthur/aa-corptools-dashboard/blob/master/CONTRIBUTING.md)
