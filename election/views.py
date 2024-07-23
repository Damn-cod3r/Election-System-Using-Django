from django.shortcuts import render, redirect
from .models import Candidate, Vote
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def candidate_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, 'Signup successful. You can now login.')
            return redirect('candidatelogin')
    return render(request, 'election/candidatesignup.html')

def candidate_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('results')  # Redirect to the vote page or another page as needed
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'election/candidatelogin.html')

def voter_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, 'Signup successful. You can now login.')
            return redirect('voterlogin')
    return render(request, 'election/votersignup.html')


def voter_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('vote')  # Redirect to the voting page or another page as needed
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'election/voterlogin.html')


def vote_view(request):
    candidates = Candidate.objects.all()
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = Candidate.objects.get(id = candidate_id)
        Vote.objects.create(candidate = candidate)
        #return redirect('results')
    return render(request, 'election/vote.html',{'candidates': candidates})

def results_view(request):
    if not request.user.is_authenticated:
        return redirect('candidatelogin')
    try:
        candidate = Candidate.objects.get(user=request.user)
    except Candidate.DoesNotExist:
        messages.error(request, 'No candidate found for this user.')
        return redirect('candidatelogin')

    votes = Vote.objects.filter(candidate=candidate)
    total_votes = votes.count()
    all_votes = Vote.objects.all()
    total_vote_count = all_votes.count()
    voters = [vote.user.username for vote in votes]

    return render(request, 'candidate_results.html', {
        'candidate': candidate,
        'total_votes': total_votes,
        'total_vote_count': total_vote_count,
        'voters': voters
    })