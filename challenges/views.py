from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    "december": "December the gift-givin' month and now you wanna rekindle our year"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
        response_data =  f"<h1>{challenge_text}</h1>"
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    
