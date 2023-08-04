# made to be as minimal as possible (hence why no comments) do note it's not a "good" code.
# e.g todo's is to make variables (REPLACE_QUERY) and more.

## [ ] USAGE: Make a links.txt file with the following contents
#   https://stackexchange.com/search?q=REPLACE_QUERY
#   https://www.google.com/search?q=REPLACE_QUERY
#   https://html.duckduckgo.com/html?q=REPLACE_QUERY
#   https://gist.github.com/search?q=REPLACE_QUERY
#   https://github.com/search?q=REPLACE_QUERY
#   https://medium.com/search?q=REPLACE_QUERY
#   https://www.youtube.com/results?search_query=REPLACE_QUERY
#   https://www.quora.com/search?q=REPLACE_QUERY
#   https://www.reddit.com/search/?q=REPLACE_QUERY

def F_getlines(in_file):
    with open(in_file,'rt') as f:
        lines = f.readlines()
    return(lines)

L_urls = F_getlines('links.txt')
import string

## [] USAGE: Change the query here
q="hello world"
for u in L_urls:
    u_clean = u.strip(string.whitespace)
    q_clean = q.replace(' ','+')
    u_clean_replaced = u_clean.replace('REPLACE_QUERY', q_clean)
    print(u_clean_replaced)

## Output will be
# https://stackexchange.com/search?q=hello+world
# ....
# https://www.youtube.com/results?search_query=hello+world
# https://www.quora.com/search?q=hello+world
# https://www.reddit.com/search/?q=hello+world

