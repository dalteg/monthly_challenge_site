from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Yeah January, you pretend to see life clearly, yearly",
    "february": "February is the time that you put the evil eye and the pride aside",
    "march": "March got you already second guessin' titles",
    "april": "April, spring is here and just like a spring, you start to spiral",
    "may": "May brings some warmer days, poolside, gettin' very tan",
    "june": "June have you movin' ice cold, goin' back and forth with a married man",
    "july": "July, that's when I found out you lied",
    "august": "August, it was \"baby\" this, \"baby\" that like you had your tubes tied",
    "september": "September, we fallin' off, but I'm still the man you tryna win over",
    "october": "October is all about me 'cause your turn should've been over",
    "november": "November got you moodboardin' for next year and you're single",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months":months
    })

def monthly_challenge_by_number(request, month):
    months =  list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challange/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name":month.capitalize()
        })
    except:
        raise Http404()
