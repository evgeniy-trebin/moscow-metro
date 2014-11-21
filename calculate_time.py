#!/usr/bin/python
# -*- coding: utf-8 -*- 

import argparse
import sys
try:
        import json
except ImportError:
        import simplejson as json
from collections import defaultdict

json_time_source="moscow-metro.json"
json_distance_source="stations.json"

def calc():
        json_data=open(json_time_source).read()
        time_data = json.loads(json_data)

        json_data=open(json_distance_source).read()
        distance_data = json.loads(json_data)

        links = time_data[0]["linkCount"]
        for l in range(1, links):
            fromStation = time_data[0]["links"][str(l)]["fromStationId"]
            toStation = time_data[0]["links"][str(l)]["toStationId"]
            line = time_data[0]["stations"][str(fromStation)]["lineId"]
            linename = time_data[0]["lines"][str(line)]["name"]
            nameFromStation = time_data[0]["stations"][str(fromStation)]["name"]
            nameToStation = time_data[0]["stations"][str(toStation)]["name"]
            time = time_data[0]["links"][str(l)]["weightTime"]
            #print "%s, %s, %s, %d, http://metro.yandex.ru/moscow?from=%d&to=%d&route=0" % (linename, nameFromStation, nameToStation, time, fromStation, toStation)
            #print distance_data[0]["stations"]
            for jline in distance_data:
                 if jline["line"] == linename:
                    #print jline["line"]
                    for station in jline["stations"]:
                        if station["station"] == nameFromStation:
                           print station["station"], station["long"], station["lat"]

def get_geo():

if len(sys.argv) > 1:
        sys.exit(1)

calc()
