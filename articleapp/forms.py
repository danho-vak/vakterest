from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):

    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable',
                                                           'style':'height:auto;'}))
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
