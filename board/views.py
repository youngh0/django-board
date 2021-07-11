from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from board.forms import BoardCreationForm, ContentCreationForm
from board.models import BoardList, BoardContent


def index(request):
    board_list = BoardList.objects.all()

    context = {
        'board_list': board_list
    }
    # print(board_list)

    return render(request, 'board_list.html', context)


def board_create(request):
    if request.method == 'POST':
        print('z')
        form = BoardCreationForm(request.POST)
        if form.is_valid():
            print('n')
            board_info = form.save(commit=False)
            board_info.user_name = 'admin'
            board_info.save()
            return redirect('board:index')
        else:
            print(messages.error(request, 'Error!'))
    else:
        form = BoardCreationForm()
    return render(request, 'board_create.html', {'form': form})

# need to implement paging
def detail(request, board_id):
    content_list = BoardContent.objects.filter(board_id_id=board_id)
    context = {
        'content_list': content_list,
        'board_id' : board_id
    }
    return render(request,'board_detail.html', {'content_list':content_list})


# need to check valid
def content_create(request, board_id):
    a = BoardList.objects.get(id=board_id)

    if request.method == 'POST':
        form = ContentCreationForm(request.POST)
        if form.is_valid():
            board_content = form.save(commit=False)
            board_content.author = 'admin'
            board_content.board_id_id = a.id
            board_content.save()
            print('gfd', board_content)
            return redirect('board:detail',board_id)
        # content_info =
    return render(request, 'board_content_create.html',{'a':a})
