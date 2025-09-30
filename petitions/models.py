from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yes_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Vote(models.Model):
    CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=3, choices=CHOICES, default='YES')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('petition', 'user')

    def __str__(self):
        return f"{self.user.username} voted {self.choice} on {self.petition.title}"