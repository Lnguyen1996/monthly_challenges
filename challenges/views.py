from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk 5k everyday",
    "march": "Learn Django for at least 20 minutes a day",
    "april": "Eat no meat for the entire month!",
    "may": "Walk 5k everyday",
    "june": "Learn Django for at least 20 minutes a day",
    "july": "Eat no meat for the entire month!",
    "august": "Walk 5k everyday",
    "september": "Learn Django for at least 20 minutes a day",
    "october": "Eat no meat for the entire month!",
    "november": "Walk 5k everyday",
    "december": "Learn Django for at least 20 minutes a day",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if (month > len(months)):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]

    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challenge_text)
