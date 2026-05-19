from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challanges = {
    'jan': "Code for 20 minutes a day!",
    'feb': "Exercise every day",
    'mar': "Go for a walk every day!",
    'apr': "Eat breakfast every day!",
    'may': "Go to sleep before 11pm every day!",
    'jun': "Tell youreself 'I matter' every day!",
    'jul': "Learn something new every day!",
    'aug': "Drink water every day!",
    'sep': "Clean something every day!",
    'oct': "Do breathing exercises every day!",
    'nov': "Learn a new skill this month!",
    'dec': "Turn off phone for 1h every day!",
}


# Create your views here.


def monthly_challange_by_num(request, month):
    months = list(monthly_challanges.keys())

    if month > len(months) or month <= 0:
        return HttpResponseNotFound(f'404 {month} is not a valid month!')
    redirect_month = months[month-1]
    # Create dynamic url
    redirect_url = reverse('monthly-challange', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        return HttpResponse(challange_text)
    except KeyError:
        return HttpResponseNotFound(f'404 {month} is not a valid month!')
