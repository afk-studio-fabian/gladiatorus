from django.db import models
from users.models import Profile  # Adjust the import based on your project structure

# Create your models here.


class FriendRequest(models.Model):
    sender = models.ForeignKey(Profile, related_name="sent_requests", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name="received_requests", on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('DECLINED', 'Declined')],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Friendship(models.Model):
    user1 = models.ForeignKey(Profile, related_name="friends1", on_delete=models.CASCADE)
    user2 = models.ForeignKey(Profile, related_name="friends2", on_delete=models.CASCADE)
    since = models.DateTimeField(auto_now_add=True)
