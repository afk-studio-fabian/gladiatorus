from django.contrib import admin
from friend.models import Friendship, FriendRequest
# Register your models here.

admin.site.register(Friendship)
admin.site.register(FriendRequest)
