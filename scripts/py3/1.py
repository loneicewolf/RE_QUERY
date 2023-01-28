
#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# Proof Of Concept
# Note; lot's of things to improve here, do NOT use this in production code!
# this code may(and most likely *will*) contain Bugs.

# sample  search query `q`
q="stutter"

# or just use
# python3 thisfile.py stutter
import sys
#[dbg] print(sys.argv[1])
q=str(sys.argv[1])

# list of sites that contain a keyword `REPLACE_QUERY`
# replace 'query'
# with the actual term

## some has additional parameters
## like google.com can have the language (&hl=en,)
## etc.

# thing to search for and
# replace with the query q
## TODO;
# review code
# add more parameters(lang,text, ..)
# i/o, input output
# functions
# more descriptive names;
# error checking
# best practices - verify
## test runs
# regex
# diff lang
# py2, ... (for compat)
# improvements; docs links; ..
# 
replace="REPLACE_QUERY"
L1=[
    "https://www.ijert.org/?s=REPLACE_QUERY",
    "https://www.researchgate.net/search?q=REPLACE_QUERY",
    "https://www.google.com/search?q=REPLACE_QUERY&hl=en",
    "https://translate.google.com/?hl=en&sl=auto&tl=ja&text=REPLACE_QUERY&op=translate",
    "https://link.springer.com/search?query=REPLACE_QUERY&searchType=publisherSearch",
    "https://stackexchange.com/search?q=REPLACE_QUERY",
    "https://github.com/search?q=REPLACE_QUERY",
    "https://en.wikipedia.org/w/index.php?title=REPLACE_QUERY&redirect=no",
    "https://www.reddit.com/search/?q=REPLACE_QUERY",
    
    # version ------------------------V  and other keywords
    "https://www.kernel.org/doc/html/v5.0/search.html?q=REPLACE_QUERY&check_keywords=yes&area=default"
]

for e in L1:
    print(e.replace(replace,q) )

