#!/usr/bin/env python3

# Collects a dictionary of words used in Reddit suggested usernames and stores it in dictionary.json.

import json
import os
import re
import requests
import sys
import time

dictionary_filename = "dictionary.json"


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, end="", flush=True, **kwargs)


def read_dictionary():
    if not os.path.isfile(dictionary_filename):
        return {'adjectives': {}, 'nouns': {}}

    with open(dictionary_filename, "r") as f:
        return json.load(f)


def write_dictionary(content):
    with open(dictionary_filename, "w") as f:
        json.dump(content, f, sort_keys=True, indent=2)


def main():
    dictionary = read_dictionary()
    pattern = re.compile("^([A-Z][a-z]*)[-_]?([A-Z][a-z]*)[-_]?\d+$")

    try:
        while True:
            usernames = requests.get("https://www.reddit.com/api/v1/generate_username.json").json()
            if usernames.get('error', None) == 429:
                time.sleep(1)
                continue

            new_words = {'adjectives': 0, 'nouns': 0}
            for username in usernames['usernames']:
                match = pattern.match(username)
                if match:
                    adjective = match.group(1)
                    previous_num_adjectives = dictionary['adjectives'].get(adjective, 0)
                    if previous_num_adjectives == 0:
                        new_words['adjectives'] += 1
                    dictionary['adjectives'][adjective] = previous_num_adjectives + 1


                    noun = match.group(2)
                    previous_num_nouns = dictionary['nouns'].get(noun, 0)
                    if previous_num_nouns == 0:
                        new_words['nouns'] += 1
                    dictionary['nouns'][noun] = previous_num_nouns + 1

            write_dictionary(dictionary)
            eprint(time.ctime())
            eprint("  Adjectives: %2d  Nouns: %2d\n" % (new_words['adjectives'], new_words['nouns']))
            time.sleep(10)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
