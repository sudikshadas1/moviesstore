from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def yes_votes(self):
        return self.votes.filter(choice="YES").count()

    def __str__(self):
        return self.title


class PetitionVote(models.Model):
    VOTE_CHOICES = (
        ("YES", "Yes"),
    )
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=10, choices=VOTE_CHOICES)

    class Meta:
        unique_together = ("petition", "user")  # prevent double-voting

    def __str__(self):
        return f"{self.user.username} voted {self.choice} on {self.petition.title}"
