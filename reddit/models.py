from django.db import models

# Create your models here.

class Reddit_Submission(models.Model):
    submission_id = models.CharField(max_length=32, unique=True)
    submission_subreddit = models.CharField(max_length=21, null=True)
    submission_time_stamp = models.CharField(max_length=32)
    submission_title = models.CharField(max_length=32)
    submission_score = models.CharField(max_length=32)
    submission_author = models.CharField(max_length=32)
    submission_url = models.CharField(max_length=32)


# class Reddit_Submission_Esclation(models.Model):
#     submission_id = models.CharField(max_length=32, unique=True)
#     submission_subreddit = models.CharField(max_length=21, null=True)
#     submission_time_stamp = models.CharField(max_length=32)
#     submission_title = models.CharField(max_length=32)
#     submission_score = models.CharField(max_length=32)
#     submission_author = models.CharField(max_length=32)
#     submission_url = models.CharField(max_length=32)

    