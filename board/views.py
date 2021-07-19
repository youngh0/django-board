from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from board.forms import BoardCreationForm, ContentCreationForm, CommentCreationForm
from board.models import BoardList, Content, Comments
from board.serializers import BoardListSerializer


def index(request):
    board_list = BoardList.objects.all()

    context = {
        'board_list': board_list
    }
    # print(board_list)

    return render(request, 'board_list.html', context)


def board_create(request):
    if request.method == 'POST':
        form = BoardCreationForm(request.POST)
        if form.is_valid():
            board_info = form.save(commit=False)
            board_info.user_name = request.user.nickname
            board_info.save()
            return redirect('board:index')
        else:
            print(messages.error(request, 'Error!'))
    else:
        form = BoardCreationForm()
    return render(request, 'board_create.html', {'form': form})


# need to implement paging
def detail(request, board_id):

    content_list = Content.objects.filter(board_id=board_id)

    board_info = BoardList.objects.get(id=board_id)


    context = {
        'content_list': content_list,
        'board_id': board_id,
        'board_info':board_info
    }
    return render(request, 'board_detail.html', context)


# need to check valid
def content_create(request, board_id):
    print(request.user.nickname)
    bid = BoardList.objects.get(id=board_id)

    if request.method == 'POST':
        form = ContentCreationForm(request.POST)

        if form.is_valid():
            board_content = form.save(commit=False)
            board_content.author = request.user.nickname
            board_content.board_id_id = bid.id
            board_content.save()

            return redirect('board:detail', board_id)
        # content_info =
    return render(request, 'board_content_create.html', {'bid': bid})


def content_delete(request, content_id):
    delete_content = Content.objects.get(id=content_id)
    delete_content.delete()
    return redirect('board:index')


def content_update(request, content_id):
    base_content = Content.objects.get(id=content_id)
    bid = base_content.board_id_id
    if request.method == 'POST':
        update_form = ContentCreationForm(request.POST)
        if update_form.is_valid():
            base_content.title = request.POST['title']
            base_content.content = request.POST['content']
            base_content.save()
            return redirect('board:detail', base_content.board_id_id)
    context = {
        'content': base_content
    }

    return render(request, 'board_content_update.html', context)


def content_detail(request,content_id):
    content = get_object_or_404(Content,pk=content_id)
    comment = Comments.objects.filter(content_id = content_id)
    context = {
        'content':content,
        'comment':comment
    }
    return render(request, 'content_detail.html', context)


def comment_create(request, content_id):
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

def comment_update(request, comment_id):
    comment_info = get_object_or_404(Comments, pk=comment_id)
    if request.method == "POST":
        update_form = CommentCreationForm(request.POST)
        if update_form.is_valid():
            content_id = comment_info.content_id

            comment_info.body = request.POST['body']
            comment_info.save()
            return redirect('board:content_detail', content_id)
    context = {
        'comment_id': comment_id,
        'body': comment_info.body
    }
    return render(request, 'comment_update.html', context)

def comment_delete(request, comment_id):
    delete_comment = Comments.objects.get(id=comment_id)
    content_id = delete_comment.content_id
    delete_comment.delete()
    return redirect('board:content_detail', content_id)

@api_view(['GET','POST'])
def api_board_list(request):
    if request.method == 'GET':
        query_set = BoardList.objects.all()
        board_list = BoardListSerializer(query_set, many=True) # json형태로 변환
        return Response(board_list.data)

    if request.method == 'POST':
        serializer = BoardListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)