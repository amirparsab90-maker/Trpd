import praw

from random import randint as r

import time

SUBREDDIT_TO_SPAM = "turningred_porn"

postsCreated = 0

errorCount = 0

reddit = praw.Reddit(client_id="cid", client_secret="cs",password="pw", user_agent="random 1.0 by u/amirparsab90",username="uname")

print(str(reddit.user.me()) + "is on a mission to DESTROY r/" + SUBREDDIT_TO_SPAM)

while True:

#    try:

    reddit.subreddit(SUBREDDIT_TO_SPAM).submit("get WRECKED btches <_=_> "*5+str(r(1000000,10000000000000000000000000000000000000000)), selftext="get destroyeddd"+str(r(100000,100000000000000000000000)), spoiler=True, nsfw=True)

    postsCreated += 1

    print("sent to r/" + SUBREDDIT_TO_SPAM + " PostCount:" + str(postsCreated))

    time.sleep(2)

#    except:

#        print("error. this may be caused because of the rate limit so we are sleeping for 9m0s0ms0ms0ns0ps")

#        errorCount += 1

#        print(errorCount)

#        for i in range(60*9):

#            time.sleep(1)

#            print("-"*17, str(i))
