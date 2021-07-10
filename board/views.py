from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from board.forms import BoardCreationForm
from board.models import BoardList


def index(request):
    board_list = BoardList.objects.all()

    context = {
        'board_list': board_list
    }
    print(board_list)

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
