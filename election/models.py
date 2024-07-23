from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Track which user voted
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Vote for {self.candidate.name} by {self.user.username} on {self.timestamp}"
