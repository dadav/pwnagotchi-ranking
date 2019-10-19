#!/usr/bin/env python3

import os
from collections.abc import MutableMapping
import argparse
import requests


API_ENDPOINT = "https://api.pwnagotchi.ai/api/v1/units"

class Termcolors:
    BG_GREEN = '\033[42m'
    FG_BLACK = '\033[30m'
    CLEAR = '\033[0m'

class Unit(dict):
    """
    Unit wrapper
    """

    def __init__(self, *args, **kwargs):
        super(Unit, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for key, value in arg.items():
                    self[key] = value

        if kwargs:
            for key, value in kwargs.items():
                self[key] = value

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Unit, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Unit, self).__delitem__(key)
        del self.__dict__[key]

# https://stackoverflow.com/questions/6027558/flatten-nested-dictionaries-compressing-keys
def _flatten(data, parent_key='', sep='_'):
    items = list()
    for key, value in data.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(_flatten(value, new_key, sep=sep).items())
        else:
            items.append((new_key, value))
    return dict(items)


def _fetch_page(page=1):
    try:
        result = requests.get(f"{API_ENDPOINT}?p={page}")
        return result.json()
    except Exception as ex:
        raise ex

def get_units(max_cnt=None):
    """
    Fetches all units

    returns list of Unit-class instances
    """
    page = 1
    result = list()
    while True:
        try:
            data = _fetch_page(page)
            if not data['units']:
                break
            for unit in data['units']:
                result.append(Unit(_flatten(unit)))
                if max_cnt and len(result) >= max_cnt:
                    return result
            page += 1
        except Exception as ex:
            break

    return result

def _sort_units_by(units, sort_key='networks'):
    return sorted(units, key=lambda x: x.get(sort_key, 0), reverse=True)

def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False
    except TypeError:
        return False

    return True

def main():
    parser = argparse.ArgumentParser(description="Compare the top pwnagotchis!")
    parser.add_argument('--max', type=int, default=10, help="Max number of units")
    parser.add_argument('--key', default="networks", help="What key should be used for sorting")
    parser.add_argument('--list', action="store_true", help="List the keys you could use for sorting")
    args = parser.parse_args()

    if args.list:
        units = get_units(max_cnt=1)
        all_keys = units[0].keys()
        for key in all_keys:
            if is_number(units[0][key]):
                print(key)
        return 0

    print("Fetching units...")
    units = get_units()
    top_units = _sort_units_by(units, sort_key=args.key)[:args.max]
    _, term_columns = os.popen('stty size', 'r').read().split()
    term_columns = int(term_columns) / 2
    max_value = top_units[0][args.key]

    for unit in top_units:
        text = f"{unit.name}: {unit.get(args.key)}"
        line_width = int(term_columns) / int(max_value) * int(unit.get(args.key))
        padding_len = int(line_width) - len(text)
        if padding_len > 0:
            padding = " " * padding_len
        else:
            padding = ""

        print(f"{Termcolors.BG_GREEN}{Termcolors.FG_BLACK}{unit.name}: {unit.get(args.key)}{padding}{Termcolors.CLEAR}")


if __name__ == "__main__":
    SystemExit(main())

