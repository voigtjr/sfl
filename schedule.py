#!/usr/bin/env python

import argparse
import json
import sys
import pprint

def load_json(filename):
    ret = None
    with open(filename) as f:
        ret = json.load(f)

    if not ret:
        print "invalid", filename
        sys.exit(1)

    return ret

def validate():
    schedule = load_json('schedule.json')
    pprint.pprint(schedule)

    draft_order = load_json('draft_order.json')
    pprint.pprint(draft_order)

def parse_args():
    p = argparse.ArgumentParser()

    return p.parse_args()

def main():
    args = parse_args()

    validate()

if __name__ == '__main__':
    main()

