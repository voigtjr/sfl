#!/usr/bin/env python

import argparse
import json
import sys
import pprint

def verify():
    schedule = None
    with open('schedule.json') as f:
        schedule = json.load(f)

    if not schedule:
        print "invalid schedule"
        sys.exit(1)

    pprint.pprint(schedule)

def parse_args():
    p = argparse.ArgumentParser()

    return p.parse_args()

def main():
    args = parse_args()

    verify()

if __name__ == '__main__':
    main()

