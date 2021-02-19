# Reddit Suggested Usernames

These scripts will collect a dictionary of words seen in usernames suggested
by Reddit on user signup.

The dictionary is stored in `dictionary.json` and the rule created for
AutoModerator is stored in `rule.yml`.

## Usage

###Run the dictionary collector

```shell
./main.py
```

Run it for as long as you like, the longer the better. Some words show up
rarely, so it may take several weeks before you can reliably find no new words.
There is no known way to ensure you've found all words, but the longer you go
without finding new words, the more confident you can be.

###Create an AutoModerator rule

```shell
./create_rule.py
```

Your new AutoModerator rule will output to `rule.yml`, which you can paste
into your subreddit's AutoModerator config.

The rule file will not update automatically, so you should run the create rule
script when you want a refreshed one.
