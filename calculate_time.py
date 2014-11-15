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

        stations = data[0]["stationCount"]
        #for s in range(1, stations):
            #print data[0]["stations"][str(s)]["name"], data[0]["stations"][str(s)]["lineId"]

        links = data[0]["linkCount"]
        for l in range(1, links):
            fromStation = data[0]["links"][str(l)]["fromStationId"]
            toStation = data[0]["links"][str(l)]["toStationId"]
            print data[0]["stations"][fromStation]["name"]
            #print data[0]["stations"][toStation]["name"]
            #print data[0]["links"][str(l)]["weightTime"]

def usage():
        print "Calculate amount of time to transfer between closest stations."

if len(sys.argv) > 1:
        usage()
        sys.exit(1)

calc()
