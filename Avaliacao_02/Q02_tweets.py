
# coding: utf-8

import re
from contextlib import redirect_stdout

#apenas URL's validas com potencial de serem fake news
pattern = re.compile(r'(RT (\W\w+)).*(https\W+t.co/\w+)')
tweets = []

with open("tweets.in", encoding="utf-8") as f:
    for line in f.readlines():
        match = pattern.match(line)
        if match != None:
            string = match.group(2)+'\t'+match.group(3)
            tweets.append(string)
    tweets.sort()

with open("tweets.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("\n".join(tweets))

