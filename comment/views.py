from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from comment.forms import CommentCreationForm
from comment.models import Comments
from django.contrib import messages


def create(request, content_id):
    if request.method == 'POST':
        print('this is post')
        comment_form = CommentCreationForm(request.POST)
        if comment_form.is_valid():
            messages.add_message(
                request,
                messages.SUCCESS,
                '성공적으로 회원가입 완료'
            )
            comment_info = comment_form.save(commit=False)
            comment_info.author = request.user.nickname
            comment_info.content_id = content_id
            comment_info.save()
        return redirect('board:content_detail', content_id)

    return redirect('board:content_detail', content_id)

# def update(request, comment_id):


def delete(request, comment_id):

    delete_comment = Comments.objects.get(id=comment_id)
    content_id = delete_comment.content_id
    delete_comment.delete()
    return redirect('board:content_detail', content_id)

def update(request, comment_id):
    comment_info = Comments.objects.get(id=comment_id)
    if request.method == "POST":
        update_form = CommentCreationForm(request.POST)
        if update_form.is_valid():
            content_id = comment_info.content_id

            comment_info.body = request.POST['body']
            comment_info.save()
            return redirect('board:content_detail', content_id)
    context = {
        'comment_id' : comment_id,
        'body':comment_info.body
    }
    return render(request,'comment_update.html',context)