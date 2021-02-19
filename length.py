#!/usr/bin/env python3

# Checks the number of entries in the dictionary.
# Useful for determining if you've found new words.

from main import read_dictionary

def main():
    dictionary = read_dictionary()
    print("Adjectives: {}".format(len(dictionary['adjectives'])))
    print("Nouns:      {}".format(len(dictionary['nouns'])))
    print("Union:      {}".format(len(list(set(dictionary['adjectives']) | set(dictionary['nouns'])))))


if __name__ == "__main__":
    main()
