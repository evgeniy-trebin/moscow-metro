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
        print(json_data)

        for stations in data:
                print stations['1']

# "stationCount":195
# "links":

calc()
