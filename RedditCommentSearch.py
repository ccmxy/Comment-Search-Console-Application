#!/usr/bin/python
import re
import argparse
from RedditCommentSearchPckg import SortComments
from RedditCommentSearchPckg import DisplayHelper

def main():

    print('Getting comments...')
    sortCommentsObject = SortComments(args=args) #initialize with args
    sortCommentsObject.sortComments() #sort the comments depending on user options (if no user or sub chosen, comments taken from r/redditdev)
    comments = sortCommentsObject.getComments()
    
    ###Do the display user chose in options
    if(args.show_text):
        for comment in comments:
            sortCommentsObject.printSelfComments()
            # print(DisplayHelper.getCommentDisplay(comment))
            # print(DisplayHelper.getCommentLink(comment))

    if(args.show_links):
        print(DisplayHelper.getCommentLinkList(comments))
    
    if(not args.show_links and not args.show_text):
        print('To display the comments or their links use options --show_links=True and/or --show_text=True')



parser = argparse.ArgumentParser(description='Search comments by subreddit, user, and/or any number of phrases. If user option is used, comments will be pulled from user\'s comment history. If neither user nor subreddit options are used, comments will be newest from redditdev will be used. No two search options need be combined.')

parser.add_argument('--search', type=str, dest='search_term_list',
                    default=None, help='Use to only retreive comments containing certain words or phrases. All phrases must be contained between quotation TOGETHER, and they must be SEPERATED by three #\'s. Example: --search="dog ### homeward bound ### dog movies".')

parser.add_argument('--user', dest='user_name', type=str,
                    default=None, help='[OPTIONAL] Use to search comments by certain user')

parser.add_argument('--subreddit', dest='subreddit', type=str,
                    default=None, help='[OPTIONAL] Only get comments from a particular subreddit')

parser.add_argument('--limit', dest='comment_limit', type=int,
                    default=None, help='[OPTIONAL] Number of comments to search user history for')

parser.add_argument('--show_text', dest='show_text', type=bool, choices=[True, False],
                    default=False, help='[OPTIONAL] <True/False> Use this to print comment text')

parser.add_argument('--show_links', dest='show_links', type=bool, choices=[True, False],
                    default=False, help='[OPTIONAL] <True/False> Use this to print links in a compact list form to output')

args = parser.parse_args()

main()
