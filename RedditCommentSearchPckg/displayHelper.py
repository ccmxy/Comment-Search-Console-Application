#!/usr/bin/python

class DisplayHelper:
    
    def getCommentLink(comment):
        return 'https://www.reddit.com/r/' + comment.subreddit.display_name + '/comments/' + comment.submission.id + '//' + comment.id

    def getCommentLinkList(comments):
        permalink_list = []
        for comment in comments:
            permalink_list.append('https://www.reddit.com/r/' + comment.subreddit.display_name + '/comments/' + comment.submission.id + '//' + comment.id)
        return permalink_list


    def getCommentDisplay(comment):
        return('\n\n~~~~~~~*******From r/' + comment.subreddit.display_name + '*******~~~~~~~\n' + comment.body)

    def getCommentDisplayList(comments):
        comment_display = []
        for comment in comments:
            comment_display.append('\n\n~~~~~~~*******From r/' + comment.subreddit.display_name + '*******~~~~~~~\n' + comment.body)
        return comment_display
