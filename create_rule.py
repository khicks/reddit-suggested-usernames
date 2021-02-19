#!/usr/bin/env python3

# Creates an AutoModerator rule with the current dictionary and outputs it to rule.yml.

import yaml
from main import read_dictionary

def main():
    dictionary = read_dictionary()
    words = list(set(dictionary['adjectives']) | set(dictionary['nouns']))
    words.sort()
    rule = {
        'type': "submission",
        'author': {
            'name (regex)': "^(({a})[-_]?){{2}}\\d+$".format(
                a="|".join(words)
            )
        },
        'action': "remove",
        'action_reason': "Reddit suggested username"
    }

    with open("rule.yml", "w") as f:
        f.write((yaml.dump(rule, sort_keys=False, indent=4)))

if __name__ == "__main__":
    main()
