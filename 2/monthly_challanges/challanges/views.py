from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challanges = {
    'january': "Code for 20 minutes a day!",
    'february': "Exercise every day",
    'march': "Go for a walk every day!",
    'april': "Eat breakfast every day!",
    'may': "Go to sleep before 11pm every day!",
    'june': "Tell youreself 'I matter' every day!",
    'july': "Learn something new every day!",
    'august': "Drink water every day!",
    'september': "Clean something every day!",
    'octtober': "Do breathing exercises every day!",
    'november': "Learn a new skill this month!",
    'december': "Turn off phone for 1h every day!",
}


# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challanges.keys())

    for month in months:
        month_path = reverse('monthly-challange', args=[month])
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>\n'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challange_by_num(request, month):
    months = list(monthly_challanges.keys())

    if month > len(months) or month <= 0:
        return HttpResponseNotFound(f'<h1>404 {month} is not a valid month!</h1>')
    redirect_month = months[month-1]
    # Create dynamic url
    redirect_url = reverse('monthly-challange', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challange(request, month):
    try:
        challange_text = monthly_challanges[month]
        response_data = render_to_string('challanges/challange.html')
        return HttpResponse(response_data)
    except KeyError:
        return HttpResponseNotFound(f'<h1>404 {month} is not a valid month!</h1>')
