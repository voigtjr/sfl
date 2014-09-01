#!/usr/bin/env python
import argparse
import json
import funcy

def verify():
    teams = None
    with open('teams.json') as f:
        teams = json.load(f)

    for name, team in teams.items():
        home = set(team['home'])
        away = set(team['away'])
        print "{}: {} games ({} home)".format(name, len(home|away), len(home))

def parse_args():
    p = argparse.ArgumentParser()

    return p.parse_args()

def main():
    args = parse_args()

    verify()

if __name__ == '__main__':
    main()

