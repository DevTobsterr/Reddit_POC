from django import forms    


class SubredditForm(forms.Form):
    # OPTIONS = (
    #     ("New", "Sort Type - New"),
    #     ("Hot", "Sort Type - Hot"),
    #     ("Top", "Sort Type - Top"),
    #     ("Rising", "Sort Type - Rising"),
    #     )
        
    subreddit = forms.CharField( min_length=3, max_length=21, label='Search', widget=forms.TextInput(attrs={'placeholder': 'r/Example'}))
    # sort_type = forms.CharField(required=True, widget=forms.Select(choices=OPTIONS))
    # result_count = forms.IntegerField(min_value=1, max_value=1000)
