from re import sub
from django.db.models.expressions import F
from django.shortcuts import redirect, render
from django.http import HttpResponse
from praw.reddit import Submission
from .forms import SubredditForm
from reddit import forms
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.urls import reverse

from reddit.models import Reddit_Submission


# Reddit Imports
import praw
import os
# End of Reddit Imports



# Create your views here.
def application_home(request):
    return render(request, "reddit/application_home.html")


def applcation_submission_esclation(request):
    return render(request, "reddit/application_submission_esclation.html")


def application_submission_search(request):
    form = SubredditForm()
    return render(request, "reddit/application_submission_search.html", {'form': form })


def application_submission_results(request):
    submission_results = Reddit_Submission.objects.all()
    return render(request, 'reddit/application_submission_results.html', {'submission_results': submission_results})


def application_delete_submission(request, submission_id):
    delete_submission_object = Reddit_Submission.objects.get(submission_id=submission_id)
    delete_submission_object.delete()
    return redirect(reverse(application_submission_results))








def application_submission_query(request):
    if request.method == "POST":
        form = SubredditForm(request.POST)

        if form.is_valid():
            reddit = praw.Reddit(
            client_id="DPn6cOtSZYZJug",
            client_secret="WQj8aPewT55hn3JQcBO0M8f1o-AqIg",
            user_agent="itoby24"
            )

            user_subreddit = form.cleaned_data['subreddit']
            user_search_type = form.cleaned_data['sort_type']
            number_of_results = form.cleaned_data['result_count']

            subreddit = reddit.subreddit(user_subreddit)
            if user_search_type == 'Hot':
                for submission in subreddit.hot(limit=number_of_results):
                    results = Reddit_Submission()
                    results.submission_id = submission.id
                    results.submission_subreddit = user_subreddit
                    results.submission_time_stamp = unix_time_converter(submission.created_utc)
                    results.submission_author = submission.author
                    results.submission_title = submission.title
                    results.submission_url = submission.url
                    results.submission_score = submission.score
                    results.save()
                return redirect(reverse(application_submission_results))
                

            elif user_search_type == "New":
                for submission in subreddit.new(limit=number_of_results):
                    results = Reddit_Submission()
                    results.submission_id = submission.id
                    results.submission_subreddit = user_subreddit
                    results.submission_time_stamp = unix_time_converter(submission.created_utc)
                    results.submission_author = submission.author
                    results.submission_title = submission.title
                    results.submission_url = submission.url
                    results.submission_score = submission.score
                    results.save()
                return redirect(reverse(application_submission_results))

            elif user_search_type == "Top":
                for submission in subreddit.top(limit=number_of_results):
                    results = Reddit_Submission()
                    results.submission_id = submission.id
                    results.submission_subreddit = user_subreddit
                    results.submission_time_stamp = unix_time_converter(submission.created_utc)
                    results.submission_author = submission.author
                    results.submission_title = submission.title
                    results.submission_url = submission.url
                    results.submission_score = submission.score
                    results.save()
                return redirect(reverse(application_submission_results))


            elif user_search_type == "Rising":
                for submission in subreddit.rising(limit=number_of_results):
                    results = Reddit_Submission()
                    results.submission_id = submission.id
                    results.submission_subreddit = user_subreddit
                    results.submission_time_stamp = unix_time_converter(submission.created_utc)
                    results.submission_author = submission.author
                    results.submission_title = submission.title
                    results.submission_url = submission.url
                    results.submission_score = submission.score
                    results.save()
                return redirect(reverse(application_submission_results))

            else:
                pass 
            return redirect(reverse(application_submission_results))
        else:
            return render(request, "reddit/application_error_404.html")
    else:
        return redirect(reverse(application_submission_results))    

            



def unix_time_converter(unix_time):
    real_time = datetime.datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')
    return real_time