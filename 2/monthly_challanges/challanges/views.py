from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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
    if month == 0:
        return HttpResponseNotFound(f'404 month {month} not found')
    try:
        months = list(monthly_challanges.keys())
        redirect_month = months[month-1]
        return HttpResponseRedirect('/challanges/' + redirect_month)
    except IndexError:
        return HttpResponseNotFound(f'404 month {month} not found')

def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        return HttpResponse(challange_text)
    except KeyError:
        return HttpResponseNotFound(f'404 {month} is not a valid month!')
