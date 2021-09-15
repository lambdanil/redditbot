#!/usr/bin/python
import praw
from praw.models import Comment
# Reddit login/app info
userAgent = ''
cID = ''
cSC= ''
userN = ''
userP =''
reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

scraped = []

# Output file for comments
save = open("./dict", "w")

subreddit = reddit.subreddit("forsen")
while True:
    for comment in subreddit.stream.comments():
        # Make sure comment is not empty (probably unnecessary)
        if not (comment.body) == "" or (comment.body) == "  " or (comment.body) == " ":
            fixed = str(comment.body)
            scraped.append(fixed)
            # Output comments to file
            save.write(";++;++;++;".join(scraped))
            print("done")
