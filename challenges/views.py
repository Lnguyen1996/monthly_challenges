from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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


def index(request):
    list_items = ""

    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()

        month_path = reverse("month-challenge", args=[month])

        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if (month > len(months)):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]

    redirect_path = reverse("month-challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")

    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
