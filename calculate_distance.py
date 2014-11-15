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

json_source="stations.json"

def calc():
        json_data=open(json_source).read()
        data = json.loads(json_data)

        url = "http://www.yournavigation.org/api/1.0/gosmore.php?format=geojson&flat=52.215676&flon=5.963946&tlat=52.2573&tlon=6.1799&v=motorcar&fast=1&layer=mapnik"
        geodata = json.load(urllib2.urlopen(url))
        print geodata["properties"]["distance"]

# www url http://yournavigation.org/?flat=55.764181234577&flon=37.625060080179&tlat=55.862806464303&tlon=37.619290139676&v=foot&fast=1&layer=mapnik

if len(sys.argv) > 1:
        sys.exit(1)

calc()
