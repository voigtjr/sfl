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
            print "derp", filename
        else:
            return ret
    except IOError:
        print "what?", filename

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
            if week == 1:
                weeks[12].add((home, away))

    validate(weeks)

    # defaultdict seems to keep the items sorted
    # in key order ... perfect
    for week, teams in weeks.items():
        print "Week {}:".format(week)
        for away, home in teams:
            print away, "at", home
        print

def validate(weeks):
    # each week: 6 games
    len_six = lambda (week, teams): len(teams) == 6

    bad_teams = funcy.remove(len_six, weeks.items())
    if bad_teams:
        print "have bad teams!!!"
        for week, teams in bad_teams:
            print week, ":", teams
        sys.exit(1)

    def tally(hg, game):
        hg[game[1]] += 1
        return hg

    all_games = funcy.cat(weeks.values())
    home_games = reduce(tally, all_games, collections.Counter())

    bad_homes = funcy.remove(lambda (x, y): y == 6, home_games.items())
    if bad_homes:
        print "have bad home game count!!!"
        for owner, homes in bad_homes:
            print owner, ":", homes
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

