## How to use? (note this is a POC for the time being)
#     GET https://raw.githubusercontent.com/loneicewolf/RE_QUERY/dev-1/scripts/bash/major_v1.sh >> abc.sh
#     bash abc.sh 
#===============================#
# This script does a few things,
## it writes 2 files:
searches_file="a.txt"
engines_file="b.txt"

# first file is containing things to search the web for
echo "hello world" >> $searches_file
echo "goodbye world" >> $searches_file

# second file contains the (*search) engines to use
echo "https://www.google.com/search?q=REPLACE_QUERY" >> $engines_file
echo "https://duckduckgo.com/?t=ffab&q=REPLACE_QUERY" >> $engines_file
echo "https://packetstormsecurity.com/search/?q=REPLACE_QUERY" >> $engines_file
echo "https://github.com/search?q=REPLACE_QUERY" >> $engines_file
echo "https://gist.github.com/search?q=REPLACE_QUERY" >> $engines_file
echo "https://stackexchange.com/search?q=REPLACE_QUERY" >> $engines_file

# the actual internals of the script
i=0;j=0; while read Q_unclean; do ((i=i+1)); Q=$(echo "$Q_unclean" | tr ' ' '+') ; (while read E; do ((j=j+1)); echo -e "$E"|sed 's/REPLACE_QUERY/'$Q'/'; done < $engines_file ) ; done < $searches_file


## Running it makes the below output
#    $ bash ax.sh 
#         https://www.google.com/search?q=hello+world
#         https://duckduckgo.com/?t=ffab&q=hello+world
#         https://packetstormsecurity.com/search/?q=hello+world
#         https://github.com/search?q=hello+world
#         https://gist.github.com/search?q=hello+world
#         https://stackexchange.com/search?q=hello+world
#         https://www.google.com/search?q=goodbye+world
#         https://duckduckgo.com/?t=ffab&q=goodbye+world
#         https://packetstormsecurity.com/search/?q=goodbye+world
#         https://github.com/search?q=goodbye+world
#         https://gist.github.com/search?q=goodbye+world
#         https://stackexchange.com/search?q=goodbye+world

# Ready to be bookmarked by just selecting it all and copy-paste into a folder in (say) Firefox.

