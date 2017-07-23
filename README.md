# my-reddit-comment-search
Reddit comment search package and example program.

With Praw 5.0.1 installed, run file with python3 and -h or --help for details.

```
$ python3 RedditCommentSearch.py --help
usage: RedditCommentSearch.py
[-h]
[--search SEARCH_TERM_LIST]
[--user USER_NAME] 
[--subreddit SUBREDDIT]
[--limit COMMENT_LIMIT]
[--show_text {True,False}]
[--show_links {True,False}]

Search comments by subreddit, user, and/or any number of phrases. If user
option is used, comments will be pulled from user's comment history. If
neither user nor subreddit options are used, comments will be newest from
redditdev will be used. No two search options need be combined.

optional arguments:
-h, --help            show this help message and exit
--search SEARCH_TERM_LIST
Use to only retreive comments containing certain words
or phrases. All phrases must be contained between
quotation TOGETHER, and they must be SEPERATED by
three #'s. Example: --search="dog ### homeward bound
### dog movies".
--user USER_NAME      [OPTIONAL] Use to search comments by certain user
--subreddit SUBREDDIT
[OPTIONAL] Only get comments from a particular
subreddit
--limit COMMENT_LIMIT
[OPTIONAL] Number of comments to search user history
for
--show_text {True,False}
[OPTIONAL] Use this to print comment text
--show_links {True,False}
[OPTIONAL] Use this to print links to output
```

### Examples

`$ python3 RedditCommentSearch.py --user=spez --show_links=True --show_text=True --limit=1000 --search="reloading ### working on" --subreddit=announcements`     

`$ python3 RedditCommentSearch.py --subreddit=pics --search="I'm sorry###That's funny###weird" --show_links=True'`
