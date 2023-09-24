from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FriendRequest, Friendship
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.

@login_required
def send_friend_request(request, profile_uuid):
    if request.method == 'POST':
        receiver = get_object_or_404(User, uuid=profile_uuid)
        if FriendRequest.objects.filter(sender=request.user.profile, receiver=receiver).exists() or \
                Friendship.objects.filter(user1=request.user.profile, user2=receiver).exists() or \
                Friendship.objects.filter(user1=receiver, user2=request.user.profile).exists():
            messages.error(request, 'Friend request already sent or you are already friends.')
            return redirect('friend:list_friends')
        
        FriendRequest(sender=request.user, receiver=receiver).save()
        messages.success(request, 'Friend request sent.')
    return redirect('friend:list_friends')

@login_required
def accept_friend_request(request, request_id):
    if request.method == 'POST':
        friend_request = get_object_or_404(FriendRequest, id=request_id)
        if friend_request.receiver == request.user:
            Friendship(user1=friend_request.sender, user2=request.user).save()
            friend_request.delete()
            messages.success(request, 'Friend request accepted.')
        else:
            messages.error(request, 'Invalid request.')
    return redirect('friend:list_pending_requests')

# Similar implementations can be done for decline_friend_request, remove_friend, list_friends, and list_pending_requests views.
