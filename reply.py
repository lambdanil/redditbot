#!/usr/bin/python
import praw
import random
import os
import time
import re
from praw.models import Comment
# Reddit login/app info
userAgent = ''
cID = ''
cSC= ''
userN = ''
userP =''
reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

# Words the bot replies to
bot_calls = [""]
banned = [""]

# Used replies
used = []

# Open file with random comments
dictfix = open("dict","r")
dictfix.readline()
line = dictfix.readline()
newline = ""
while line != "":
    line = dictfix.readline()
    newline = newline+line
# Put comments into a list
bot_quotes = list(newline.split(";++;++;++;"))

# Main loop
subreddit = reddit.subreddit("forsen")
for comment in subreddit.stream.comments():
    dictfix = open("dict","r")
    dictfix.readline()
    line = dictfix.readline()
    newline = ""
    while line != "":
        line = dictfix.readline()
        newline = newline+line
    # Put comments into a list
    bot_quotes = list(newline.split(";++;++;++;"))
    # If comments is saved, it has already been replied to
    if not comment.saved and comment.author.name != userN:
        called = 0
        # Checks if bot was called
        for call in bot_calls:
            if (call in comment.body.lower()):
                bot_reply = random.choice(bot_quotes)
                attempts = 0
                # Prevents repetition
                while (bot_reply in used) or re.compile('|'.join(banned),re.IGNORECASE).search(bot_reply.lower()):
                    bot_reply = random.choice(bot_quotes)
                    time.sleep(0.1)
                    attempts += 1
                    if attempts > len(used)+20:
                        used = []
                used.append(bot_reply)
                called = 1
                if call == bot_calls[-1]:
                    break
        # Reply to the post (only if the bot was called) 
        if called == 1:
            comment.reply(bot_reply)
            comment.save()
            print("------------vvvvvvvv")
            print(comment.body)
            print("vvvvvvvvvvvvvvvvvvvv")
            print(bot_reply)
            print("------------\nReply Sent\n------------")
            time.sleep(2)
    dictfix.close()
