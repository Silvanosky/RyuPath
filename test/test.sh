#!/bin/bash

python channel_overrides.py --connect /dev/ttyUSB0,57600 "${@}"
