#!/usr/bin/python

import argparse
import sys
try:
        import json
except ImportError:
        import simplejson as json
from collections import defaultdict

json_source="moscow-metro.json"

def calc():
        json_data=open(json_source).read()
        data = json.loads(json_data)

        links = data[0]["linkCount"]
        for l in range(1, links):
            fromStation = data[0]["links"][str(l)]["fromStationId"]
            toStation = data[0]["links"][str(l)]["toStationId"]
            line = data[0]["stations"][str(fromStation)]["lineId"]
            linename = data[0]["lines"][str(line)]["name"]
            nameFromStation = data[0]["stations"][str(fromStation)]["name"]
            nameToStation = data[0]["stations"][str(toStation)]["name"]
            time = data[0]["links"][str(l)]["weightTime"]
            print "%s, %s, %s, %d, http://metro.yandex.ru/moscow?from=%d&to=%d&route=0" % (linename, nameFromStation, nameToStation, time, fromStation, toStation)

if len(sys.argv) > 1:
        sys.exit(1)

calc()
