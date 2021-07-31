from django.shortcuts import render, redirect
from .models import *

def userList(request):
    context ={}
    users = Users.objects.all()
    context = {'users':users}
    return render(request, 'surprisebox/list.html', context)


def userDetail(request, username):
    visit_Surprise_Numbers = [8,10,13,15,16] # Hard Code
    try:
        userData = Users.objects.get(username=username)
    except:
        userData = False
    visitor_count = Users.objects.last().id
    context ={}


    if userData:
        message = 'User:  ' + userData.username +  ' already visited  &  '
        if userData.is_winner == True:
            message = message + 'Winner'
        else:
            message = message + 'Loser'

    else:
        visitor_count = Users.objects.last().id + 1
        if (visitor_count in visit_Surprise_Numbers):
            UserCreated = Users(username=username,is_winner=True)
            message ='Winner'
        else:
            UserCreated = Users(username=username,is_winner=False)
            message ='Loser'
        UserCreated.save()
        message = 'New User Visited : ' + UserCreated.username + '  &  ' + message 

    context ={'message':message,'visitor_count': visitor_count,'username':username,'visit_Surprise_Numbers':visit_Surprise_Numbers}
    return render(request, 'surprisebox/user.html', context)


def index(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        return redirect('user-detail/'+username+'/') 

    return render(request, 'surprisebox/index.html', context)

