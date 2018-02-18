# kapacitor

This bundle will install [kapacitor](https://www.influxdata.com/time-series-platform/kapacitor/) as part of the TICK stack.

## Requirements

* Bundles:
  * [dnf](https://github.com/rullmann/bundlewrap-dnf)
  * [influxdb](https://github.com/rullmann/bundlewrap-influxdb)

## Setup notes

A pre-configured influxdb is required. Please find the details inside the influxdb bundle.

## Integrations

* Bundles:
  * [telegraf](https://github.com/rullmann/bundlewrap-telegraf)

## Metadata

    'metadata': {
        'kapacitor': {
            'influxdb_url': 'http://127.0.0.1:8086', # optional
            'username': 'telegraf', # optional, username for influxdb
            'password': 'mysupersecretpassword', # required, password for influxdb
            'smtp_from': '', # required, send alerts from this address
            'smtp_to': '', # required, send alerts to this address
        },
    }
