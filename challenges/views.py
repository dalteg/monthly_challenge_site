from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    "january":"Eat no meat for the  entire  month!",
    "february": "We keep locking in!",
    "march": "we look forward to april",
    "april": "We lockin",
    "may": "We lockin",
    "june": "We lockin",
    "july": "We lockin",
    "august": "We lockin",
    "september": "We lockin",
    "october": "We lockin",
    "november": "We lockin",
    "december": "We lockin"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months =  list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month + "/")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")