from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Django Developers'},
    {'id': 3, 'name': 'React Developers'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for dic in rooms:
        if dic['id'] == int(pk):
            room = dic
    context = {'room': room}
    return render(request, 'base/room.html', context)
