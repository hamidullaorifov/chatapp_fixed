from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Message,Chat
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.


def chatting(request,id):
    other_user = get_object_or_404(User,id=id)
    if not Chat.objects.filter(Q(user1=request.user,user2=other_user)| Q(user2=request.user,user1=other_user)).exists():
        create_chat(request,id)
    context={
        'other_user':other_user,
        'this_user':request.user,
        'id':request.user.id
    }
    return render(request,'chat/history.html',context)

    


def send(request):
    senderid = request.POST['sender']
    receiverid = request.POST['receiver']
    sender = get_object_or_404(User,id=senderid)
    receiver = get_object_or_404(User,id=receiverid)
    message = request.POST['message']
    print(senderid,receiverid,message)
    msg = Message.objects.create(sender=sender,receiver=receiver,messageText=message)
    msg.save()



def getChats(request,id):
    users = []

    user = get_object_or_404(User,id=id)
    chats = Chat.objects.filter(user1=user)
    for chat in chats:
        users.append(chat.user2)

    chats = Chat.objects.filter(user2=user)
    for chat in chats:
        users.append(chat.user1)
   
    users_list = [
        {'user_id':user.id,
        'username':user.username}
        for user in users
    ]
    return JsonResponse({'users':users_list})

def getContacts(request):
    query = request.GET.get('q')
    users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
    users_list = [
        {'user_id':user.id,
        'username':user.username}
        for user in users
    ]
    return JsonResponse({'users':users_list})


def getMessages(request):
    id = request.GET.get('id')
    user = request.user
    other_user = get_object_or_404(User,id=id)
    messages = Message.objects.filter(Q(sender=user,receiver=other_user)|Q(sender=other_user,receiver=user))
    messages_list = [
        {
            'messageText':message.messageText,
            'sent':message.sender==user,
        }for message in messages
    ]
    return JsonResponse({'messages':messages_list})


@login_required
def index(request):

    context ={
        'id':request.user.id
        # 'users':users
    }
    return render(request,'chat/base.html',context)


def create_chat(request,id):
    user1 = request.user
    user2 = get_object_or_404(User,id=id)
    chat = Chat.objects.create(user1=user1,user2=user2)
    chat.save()