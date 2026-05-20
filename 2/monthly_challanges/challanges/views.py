from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse


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
    'october': "Do breathing exercises every day!",
    'november': "Learn a new skill this month!",
    'december': None,
}


# Create your views here.


def index(request):
    months = list(monthly_challanges.keys())

    return render(request, 'challanges/index.html', {
        'months': months,
    })


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
        return render(request, 'challanges/challange.html', {
            'month_name': month,
            'text': challange_text,
        })
    except KeyError:
        raise Http404()
