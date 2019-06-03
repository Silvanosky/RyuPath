#!/bin/bash

python goto.py --connect /dev/ttyUSB0,57600 --path "${@}"
