#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from dronekit import connect, VehicleMode, LocationLocal
import time

import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    while vehicle.armed:
        vehicle.armed = False

    vehicle.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#Set up option parsing to get connection string
import argparse
parser = argparse.ArgumentParser(description='Example showing how to set and clear vehicle channel-override information.')
parser.add_argument('--connect',
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
parser.add_argument('--path',
                   help="Select path")

args = parser.parse_args()

current_path = int(args.path)
print("Starting path number: %d" % current_path)

connection_string = args.connect

# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=False)

time.sleep(5)

print("Starting")

vehicle.mode = VehicleMode("GUIDED")

vehicle.armed = True
# Confirm vehicle armed before attempting to take off
while not vehicle.armed:
    print(" Waiting for arming...")
    time.sleep(0.1)

def Trajectoire1():

	print("Set default/target airspeed to 3")
	vehicle.airspeed = 3

	point1 = LocationGlobal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(2)

	point1 = LocationLocal(0, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(3, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(3, 4, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(0, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(15)

	point1 = LocationLocal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(3)

def Trajectoire2():
	print("Set default/target airspeed to 3")
	vehicle.airspeed = 3

	point1 = LocationLocal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(2)

	point1 = LocationLocal(0, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(0, 2, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(1.5, 2, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(8)

	point1 = LocationLocal(1.5, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(3, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(3, 2, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(4, 2, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(4, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(0, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(10)

	point1 = LocationLocal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(2)

def Trajectory3():
	print("Set default/target airspeed to 3")
	vehicle.airspeed = 3

	point1 = LocationLocal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(2)

	point1 = LocationLocal(0, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(3)

	point1 = LocationLocal(5, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(15)

	point1 = LocationLocal(0, 0, 0.5)
	vehicle.simple_goto(point1)

	time.sleep(15)

	point1 = LocationLocal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(3)

def Trajectoire4():
	print("Set default/target airspeed to 3")
	vehicle.airspeed = 3

	point1 = LocationLocal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(2)

	point1 = LocationLocal(0, 0, 0.7)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(1, 0, 0.7)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(1, 0, 0.2)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(2, 0, 0.2)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(3, 0, 0.7)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(4, 0, 0.7)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(4, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(5)

	point1 = LocationLocal(0, 0, 0)
	vehicle.simple_goto(point1)

	time.sleep(15)


if current_path == 1:
	 Trajectoire1()
elif current_path == 2:
	 Trajectoire2()
elif current_path == 3:
	 Trajectoire3()
elif current_path == 4:
	 Trajectoire4()

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()

