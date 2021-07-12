from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
    print(board_id)
    bid = get_object_or_404(BoardList, pk=board_id)
    print(bid)
    content_list = bid.boardcontent_set.filter(board_id=board_id)
    print(content_list)
    context = {
        'content_list': content_list,
        'board_id' : board_id
    }
    return render(request,'board_detail.html', context)


# need to check valid
def content_create(request, board_id):
    print(request.user.nickname)
    a = BoardList.objects.get(id=board_id)

    if request.method == 'POST':
        form = ContentCreationForm(request.POST)
        print(form)
        if form.is_valid():
            board_content = form.save(commit=False)
            board_content.author = request.user.nickname
            board_content.board_id_id = a.id
            board_content.save()
            print('gfd', board_content)
            return redirect('board:detail',board_id)
        # content_info =
    return render(request, 'board_content_create.html',{'a':a})
