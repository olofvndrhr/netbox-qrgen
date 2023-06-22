# netbox-qrgen

NetBox plugin to generate QR codes for assets

CI/CD

[![status-badge](https://img.shields.io/drone/build/olofvndrhr/netbox-qrgen?label=ci&server=https%3A%2F%2Fci.44net.ch)](https://ci.44net.ch/olofvndrhr/netbox-qrgen)
[![Last Release](https://img.shields.io/github/release-date/olofvndrhr/netbox-qrgen?label=last%20release)](https://github.com/olofvndrhr/netbox-qrgen/releases)
[![Version](https://img.shields.io/github/v/release/olofvndrhr/netbox-qrgen?label=git%20release)](https://github.com/olofvndrhr/netbox-qrgen/releases)
[![Version PyPi](https://img.shields.io/pypi/v/netbox-qrgen?label=pypi%20release)](https://pypi.org/project/netbox-qrgen/)

Code Analysis

[![Quality Gate Status](https://sonarqube.44net.ch/api/project_badges/measure?project=olofvndrhr%3Anetbox-qrgen&metric=alert_status&token=a9eb06d77cd040196db73654fa8916d8a9ad9172)](https://sonarqube.44net.ch/dashboard?id=olofvndrhr%3Anetbox-qrgen)
[![Bugs](https://sonarqube.44net.ch/api/project_badges/measure?project=olofvndrhr%3Anetbox-qrgen&metric=bugs&token=a9eb06d77cd040196db73654fa8916d8a9ad9172)](https://sonarqube.44net.ch/dashboard?id=olofvndrhr%3Anetbox-qrgen)

Meta

[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)
[![Linter](https://img.shields.io/badge/linter-ruff-red)](https://github.com/charliermarsh/ruff)
[![Types](https://img.shields.io/badge/types-pyright-blue)](https://github.com/microsoft/pyright)
[![License](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://snyk.io/learn/what-is-mit-license/)
[![Compatibility](https://img.shields.io/pypi/pyversions/netbox-qrgen)](https://pypi.org/project/netbox-qrgen/)

---

## Description

test

## Features (not complete)

-   test

## Compatibility

This plugin requires Netbox version >=3.3 to work. (Older versions are not tested)

| NetBox Version | Plugin Version |
| -------------- | -------------- |
| 3.3            | >=0.0.1        |
| 3.4            | >=0.0.1        |
| 3.5            | >=0.0.1        |

## Installing

Review the [official Netbox plugin documentation](https://docs.netbox.dev/en/stable/plugins/#installing-plugins) for installation instructions.

### With pip ([pypi](https://pypi.org/project/netbox-qrgen/))

```sh
/opt/netbox/venv/bin/pip install --no-warn-script-location netbox-qrgen
```

### In the netbox docker container

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

```sh
FROM netboxcommunity/netbox:v3.5.4

RUN \
    && /opt/netbox/venv/bin/pip install --no-warn-script-location \
    netbox-qrgen
```

## Configuration

```yml
PLUGINS = [
    'netbox_qrgen_'
]

# default settings
PLUGINS_CONFIG = {
    "netbox_qrgen": {
        "qr_with_text": True,
        "qr_text_fields": ["name", "serial"],
        "qr_font": "Tahoma",
        "qr_custom_text": None,
        "qr_text_location": "right",
        "qr_version": 2,
        "qr_error_correction": 1,
        "qr_box_size": 6,
        "qr_border_size": 4,
        "labels": {
            "dcim.cable": [
                "tenant",
                "a_terminations.device",
                "a_terminations.name",
                "b_terminations.device",
                "b_terminations.name",
            ],
            "dcim.rack": [
                "tenant",
                "site",
                "facility_id",
                "name",
            ],
            "dcim.device": ["tenant", "name", "serial"],
            "dcim.inventoryitem": ["tenant", "name", "serial"],
            "circuits.circuit": ["tenant", "name", "serial"],
        },
    },
}
```

### Custom settings

| Setting               | Type        | Default value        | Description                                                                                                                                                                                                                                                                          |
| --------------------- | ----------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `qr_with_text`        | `bool`      | `True`               | Generate a text with the specified infos besides the QR code.                                                                                                                                                                                                                        |
| `qr_text_fields`      | `list[str]` | `["name", "serial"]` | Fields to add as a text to the QR code. All object properties can be used.                                                                                                                                                                                                           |
| `qr_font`             | `str`       | `'Tahoma'`           | Font to use to generate the text. Included fonts: `ArialBlack`,`ArialMT`,`JetBrainsMono`,`JetBrainsMonoBold`,`Tahoma`,`TahomaBold`.                                                                                                                                                  |
| `qr_custom_text`      | `str`       | `None`               | Custom text to be added to every QR code.                                                                                                                                                                                                                                            |
| `qr_text_location`    | `str`       | `right`              | Where the text fields are rendered relative to the QR code                                                                                                                                                                                                                           |
| `qr_version`          | `int`       | `2`                  | An integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21x21 matrix). More details [here](https://www.qrcode.com/en/about/version.html)                                                                                                        |
| `qr_error_correction` | `int`       | `1`                  | Error corrector for the QR code. Available options: `1`,`2`,`3`,`4`. See [the package docs](https://github.com/lincolnloop/python-qrcode#advanced-usage) for more details. The integer mapping is [here](https://github.com/lincolnloop/python-qrcode/blob/main/qrcode/constants.py) |
| `qr_box_size`         | `int`       | `6`                  | Controls how many pixels each "box" of the QR code is                                                                                                                                                                                                                                |
| `qr_border_size`      | `int`       | `4`                  | controls how many boxes thick the border should be (the default is 4, which is the minimum according to the specs).                                                                                                                                                                  |

## Contribution / Bugs

For suggestions for improvement, just open a pull request.

If you encounter any bugs, also just open an issue with a description of the problem.

## TODO's

-   test

```

```
