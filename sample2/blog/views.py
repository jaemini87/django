from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
import django
import sqlite3 as sql
import sys
from datetime import date,timedelta
from blog.models import Bet
from blog.models import Counter
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
# Create your views here.
def picks(request):
    try:
        fin = open("/home/ssangcom/django/static/blog/computer_picks.txt",'r')
        num_bets = int(fin.readline())
    except IOError:
        num_bets = 0
    posts = Bet.objects.all()
    for post in posts:
        post.delete()
    for ii in range(0,num_bets):
        teamA = fin.readline() 
        teamB = fin.readline() 
        betSlip = fin.readline() 
        odds = fin.readline()  
        betAmount = fin.readline()  

        Bet.objects.create(TeamA=teamA,TeamB=teamB,BetSlip=betSlip,
                Odds=odds,BetAmount=betAmount)
        
    fin.close()
    posts = Bet.objects.all()
    for post in posts:
        post.save()
    return render(request,'blog/sports_picks.html',{'posts':posts})
def tk_top(request):
    count = Counter.objects.first()
    date_now = date.today()
    if count.hit_date.isoformat()[-1] == date_now.isoformat()[-1]:
        count.hit_today += 1
    else:
        count.hit_today = 1
    count.hit_total += 1
    count.hit_date = date.today()
    count.save() 
    return render(request,'blog/tk_sports_top.html',{'hit_count':count})
def tk_picks(request):
    try:
        fin = open("/home/ssangcom/django/static/blog/tk_computer_picks.txt",'r')
        num_bets = int(fin.readline())
    except IOError:
        num_bets = 0
    posts = Bet.objects.all()
    for post in posts:
        post.delete()
    for ii in range(0,num_bets):
        teamA = fin.readline() 
        teamB = fin.readline() 
        betSlip = fin.readline() 
        odds = fin.readline()  
        betAmount = fin.readline()  

        Bet.objects.create(TeamA=teamA,TeamB=teamB,BetSlip=betSlip,
                Odds=odds,BetAmount=betAmount)
        
    fin.close()
    posts = Bet.objects.all()
    for post in posts:
        post.save()
    return render(request,'blog/tk_sports_picks.html',{'posts':posts})

def top(request):
    count = Counter.objects.first()
    date_now = date.today()
    if count.hit_date.isoformat()[-1] == date_now.isoformat()[-1]:
        count.hit_today += 1
    else:
        count.hit_today = 1
    count.hit_total += 1
    count.hit_date = date.today()
    count.save() 
    return render(request,'blog/sports_top.html',{'hit_count':count})
    #return render(request,'blog/sports_top.html')
def post_list_admin(request):
    try:
        fin = open("/home/ssangcom/django/static/blog/computer_picks.txt",'r')
        num_bets = int(fin.readline())
    except IOError:
        num_bets = 0
    posts = Bet.objects.all()
    for post in posts:
        post.delete()
    for ii in range(0,num_bets):
        teamA = fin.readline() 
        teamB = fin.readline() 
        betSlip = fin.readline() 
        odds = fin.readline()  
        betAmount = fin.readline()  

        Bet.objects.create(TeamA=teamA,TeamB=teamB,BetSlip=betSlip,
                Odds=odds,BetAmount=betAmount)
        
    fin.close()
    posts = Bet.objects.all()
    for post in posts:
        post.save()
    return render(request,'blog/post_list.html',{'posts':posts})
def post_list(request):

    try:
        fin = open("/home/ssangcom/django/static/blog/computer_picks.txt",'r')
        num_bets = int(fin.readline())
    except IOError:
        num_bets = 0
    posts = Bet.objects.all()
    for post in posts:
        post.delete()
    for ii in range(0,num_bets):
        if ii % 5 != 1 and ii % 5 != 3:
            teamA = fin.readline() 
            teamB = fin.readline() 
            betSlip = fin.readline() 
            odds = fin.readline()  
            betAmount = fin.readline()  

            Bet.objects.create(TeamA=teamA,TeamB=teamB,BetSlip=betSlip,
                    Odds=odds,BetAmount=betAmount)
    fin.close()     
    posts = Bet.objects.all()
    for post in posts:
        post.save()
    return render(request,'blog/post_list.html',{'posts':posts})
