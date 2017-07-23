import re
import copy
import praw

class SortComments:

    def __init__(self, args):
        self.args = copy.deepcopy(args) if args else {}
        self.comments = []
    
    def sortComments(self):
        args = self.getArgs()
        
        #Fill client_id, client_secret, and user_agent with valid credentials
        r = praw.Reddit(client_id='<client_id>',
                        client_secret='<client_secret>',
                        user_agent='<user_agent>')


        if(args.user_name):
            self.comments = r.redditor(args.user_name).comments.new(limit=args.comment_limit)
            if(args.subreddit):
                self.subredditComments(args.subreddit)
        elif(args.subreddit):
            self.comments = r.subreddit(args.subreddit).comments(limit=args.comment_limit)

        else:
            self.comments = r.subreddit('redditdev').comments(limit=args.comment_limit)
    
        if(args.search_term_list):
            self.wordSearchComments(args.search_term_list)

    def printSelfComments(self):
        comments = self.getComments()
        for comment in comments:
            print(comment.body)
    
    def printArgs(self):
        args = self.getArgs()
        if(args.user_name):
            print(args.user_name)

    def getComments(self):
        return self.comments

    def getArgs(self):
        return self.args
    
    def wordSearchComments(self, search_list):
        comments_list = []
        search_list = search_list.split("###")
        comments = self.getComments()
        for comment in self.comments:
            comment_text = comment.body.lower()
            if any(phrase.lower() in comment_text for phrase in search_list):
                comments_list.append(comment)
        self.comments = comments_list

    def subredditComments(self, input_subreddit_name):
        output_comments_list = []
        comments = self.getComments()
        for comment in comments:
            if (input_subreddit_name.lower() == comment.subreddit.display_name.lower()):
                output_comments_list.append(comment)
        self.comments = output_comments_list





