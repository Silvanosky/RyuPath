#!/bin/bash

mavproxy.py --master=/dev/ttyUSB1,57600 --out=udpin:0.0.0.0:14550
