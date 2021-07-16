from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from comment.forms import CommentCreationForm


def create(request, content_id):
    if request.method == 'POST':
        print('this is post')
        comment_form = CommentCreationForm(request.POST)
        if comment_form.is_valid():

            comment_info = comment_form.save(commit=False)
            comment_info.author = request.user.nickname
            comment_info.content_id = content_id
            comment_info.save()
        return redirect('board:content_detail', content_id)

    return redirect('board:content_detail', content_id)