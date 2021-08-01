from re import sub
from django.db.models.expressions import F
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubredditForm
from reddit import forms
from django.core.exceptions import ObjectDoesNotExist

from reddit.models import Reddit_Submission


# Reddit Imports
import praw
import os





# Create your views here.
def application_home(request):
    return render(request, "reddit/application_home.html")


def application_submisson_search(request):
    form = SubredditForm()
    return render(request, "reddit/application_submission_search.html", {'form': form })







def application_submisson_results(request):
    if request.method == "POST":
        form = SubredditForm(request.POST)

        if form.is_valid():
            user_subreddit = form.cleaned_data['subreddit']
            
            reddit = praw.Reddit(
            client_id="DPn6cOtSZYZJug",
            client_secret="WQj8aPewT55hn3JQcBO0M8f1o-AqIg",
            user_agent="itoby24"
            )

            subreddit = reddit.subreddit(user_subreddit)

            for submission in subreddit.new(limit=1):
                reddit_submission = Reddit_Submission(
                    submission_id = submission.id,
                    submission_time_stamp = submission.created_utc,
                    submission_title = submission.title,
                    submission_score = submission.score,
                    submission_author = submission.author,
                    submission_url = submission.url,
                )
                try: 
                    checking_for_duplicate = Reddit_Submission.objects.get(submission_id=submission.id)
                except ObjectDoesNotExist:
                    reddit_submission.save()

            submission_results = Reddit_Submission.objects.all()
            
            return render(request, 'reddit/application_submission_results.html', {'submission_results': submission_results})
        else:
            return render(request, "reddit/application_error_404.html")
    else:
        submission_results = Reddit_Submission.objects.all()
        return render(request, 'reddit/application_submission_results.html', {'submission_results': submission_results})

            













# Reddit Class - Code in releation to Reddit Only.
class Reddit:
    def Reddit_Submission(self, subreddit):
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



   
