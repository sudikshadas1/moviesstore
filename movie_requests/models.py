from django.db import models
from django.contrib.auth.models import User

class MovieRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=200)
    movie_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_name} (by {self.user.username})"
