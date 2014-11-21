#!/usr/bin/python
# -*- coding: utf-8 -*- 

import argparse
import urllib2
import sys
try:
        import json
except ImportError:
        import simplejson as json
from collections import defaultdict

json_time_source="moscow-metro.json"
json_distance_source="stations.json"

def calculate():
        json_data=open(json_time_source).read()
        time_data = json.loads(json_data)

        links = time_data[0]["linkCount"]
        for l in range(1, links):
            fromStation = time_data[0]["links"][str(l)]["fromStationId"]
            toStation = time_data[0]["links"][str(l)]["toStationId"]
            line = time_data[0]["stations"][str(fromStation)]["lineId"]
            linename = time_data[0]["lines"][str(line)]["name"]
            nameFromStation = time_data[0]["stations"][str(fromStation)]["name"]
            nameToStation = time_data[0]["stations"][str(toStation)]["name"]
            time = time_data[0]["links"][str(l)]["weightTime"]

            tlat = get_coord(linename, nameFromStation, "lat")
            tlon = get_coord(linename, nameFromStation, "long")
            flat = get_coord(linename, nameToStation, "lat")
            flon = get_coord(linename, nameToStation, "long")
            
            if (flat, flon, tlat, tlon):
               print "   ", flat, flon, tlat, tlon, nameFromStation, nameToStation
               #print "%s, %s, %s, %d, http://metro.yandex.ru/moscow?from=%d&to=%d&route=0, %s" % (linename, nameFromStation, nameToStation, time, fromStation, toStation, get_distance(flat, flon, tlat, tlon))

def get_coord(lnname, stname, coordinate):
        json_data=open(json_distance_source).read()
        distance_data = json.loads(json_data)

        for jline in distance_data:
            if jline["line"] == lnname:
               for station in jline["stations"]:
                   if station["station"] == stname:
                      return station[coordinate]

def get_distance(flat, flon, tlat, tlon):
        url = "http://www.yournavigation.org/api/1.0/gosmore.php?format=geojson&flat=" \
        + flat + "&flon=" + flon + "&tlat=" + tlat + "&tlon=" + tlon + "&v=foot&fast=1&layer=mapnik"
        geodata = json.load(urllib2.urlopen(url))
        print geodata["properties"]["distance"]

if len(sys.argv) > 1:
        sys.exit(1)

calculate()
