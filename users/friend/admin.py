from django.contrib import admin
from users.friend.models import Friendship, FriendRequest
# Register your models here.

admin.site.register(Friendship)
admin.site.register(FriendRequest)
