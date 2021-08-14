from django.shortcuts import render, redirect
from .models import *
from .serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import  Response

@api_view(['GET'])
def userListAPI(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

def userList(request):
    context ={}
    return render(request, 'surprisebox/list.html', context)


@api_view(['GET', 'POST'])
def userDetailAPI(request, username):
    visit_Surprise_Numbers = [8,10,13,15,16] # Hard Code
    try:
        userData = Users.objects.get(username=username)
    except:
        userData = False

    if userData:
        visitor_count = Users.objects.last().id
        serializer = UsersSerializer(userData, many=False)
    else:
        visitor_count = Users.objects.last().id + 1
        if (visitor_count in visit_Surprise_Numbers):
            UserCreated = Users(username=username,is_winner=True)
        else:
            UserCreated = Users(username=username,is_winner=False)

        UserCreated.save()
        serializer = UsersSerializer(UserCreated)

    responsejson={'visitor_count':visitor_count,'visit_Surprise_Numbers':visit_Surprise_Numbers}
    responsejson.update(serializer.data)
    return Response(responsejson)
        


def userDetail(request, username):
    context={'username':username}
    return render(request, 'surprisebox/user.html', context)


def index(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        return redirect('user-detail/'+username+'/') 

    return render(request, 'surprisebox/index.html', context)

