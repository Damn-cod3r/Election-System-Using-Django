from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # You can add additional fields specific to voters if needed

    def __str__(self):
        return self.user.username

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)  # Track which voter voted
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote for {self.candidate.name} by {self.voter.user.username} on {self.timestamp}"
