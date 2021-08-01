import praw
import os




# Reddit Class - Code in releation to Reddit Only.
class Reddit:
    def Reddit_Submission(self):
        reddit = praw.Reddit(
        client_id="DPn6cOtSZYZJug",
        client_secret="WQj8aPewT55hn3JQcBO0M8f1o-AqIg",
        user_agent="itoby24"
        )

        subreddit = reddit.subreddit('Citrix')

        for submission in subreddit.new():
            print(submission.title)
            print(submission.url)
            print(submission.over_18)



   
