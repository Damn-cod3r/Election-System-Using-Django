from django.urls import path
from .views import home, vote_view, results_view, candidate_signup, candidate_login, voter_signup, voter_login

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('vote/', vote_view, name='vote'),
    path('results/', results_view, name='results'),
    path('candidatesignup/', candidate_signup, name='candidatesignup'),
    path('candidatelogin/', candidate_login, name='candidatelogin'),
    path('votersignup/', voter_signup, name='votersignup'),
    path('voterlogin/', voter_login, name='voterlogin'),
]
