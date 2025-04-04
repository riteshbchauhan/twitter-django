from django.shortcuts import render
from .models import Twitter
from .forms import TwitterForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SearchForm
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Twitter.objects.all().order_by('-create')
    return render(request, 'tweet_list.html', {'tweets' : tweets} )

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TwitterForm(request.POST, request.FILES)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TwitterForm()
    return render(request, 'tweet_form.html', {'form' : form} )

@login_required
def tweet_update(request, Twitter_id):
    tweet = get_object_or_404(Twitter, pk = Twitter_id, user = request.user)
    
    if request.method == "POST":
        form = TwitterForm(request.POST, request.FILES, instance = tweet)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TwitterForm(instance = tweet)
    return render(request, 'tweet_form.html', {'form' : form} )

@login_required
def tweet_delete(request, Twitter_id):
    tweet = get_object_or_404(Twitter, pk = Twitter_id, user = request.user)

    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_delete.html', {'tweet' : tweet} )

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def search(request):
    form = SearchForm(request.GET)  # Bind the form with GET data
    tweets = []  # Initialize the list to store tweet results

    if form.is_valid():
        query = form.cleaned_data['query']
        
        # Perform search: searching for the query in tweet's text or user name
        tweets = Twitter.objects.filter(Q(text__icontains=query) | Q(user__username__icontains=query))

    return render(request, 'search_results.html', {'form': form, 'tweets': tweets})
