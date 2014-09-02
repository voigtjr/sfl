#!/usr/bin/env python

import argparse
import json
import sys
import pprint
import funcy
import collections

def load_json(filename):
    try:
        with open(filename) as f:
            ret = json.load(f)

        if not ret:
            print "invalid", filename
        else:
            return ret
    except IOError:
        print "ioerror", filename

    sys.exit(1)

def print_weeks():
    schedule = load_json('schedule.json')
    draft_order = load_json('draft_order.json')

    schedule = zip(draft_order, schedule)

    weeks = collections.defaultdict(set)

    for left, sched in schedule:
        for week, right in zip(sched, draft_order):
            home = right
            away = left
            if week < 0:
                week *= -1
                away = right
                home = left
            weeks[week].add((away, home))

    validate(weeks)

    # need to sort the weeks...
    for week, teams in weeks.items():
        print "Week {}:".format(week)
        for away, home in teams:
            print away, "at", home
        print

def validate(weeks):
    # each week: 6 games
    has_six = lambda (week, teams): len(teams) == 6

    bad_teams = funcy.remove(has_six, weeks.items())
    if bad_teams:
        print "have bad teams!!!"
        for week, teams in bad_teams:
            print week, ":", teams
        sys.exit(1)
    return

def parse_args():
    p = argparse.ArgumentParser()

    return p.parse_args()

def main():
    args = parse_args()

    print_weeks()

if __name__ == '__main__':
    main()

