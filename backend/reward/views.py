from django.core.mail.backends import console
from django.shortcuts import render
from rest_framework import viewsets, generics  # add this
# from .serializers import RemSerializer, AllowancesSerializer  # add this
from .serializers import RemSerializer
from .models import Rem
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse
from .forms import RemForm
from django.db.models import Q
import datetime


def index(request):
    return render(request, "index.html", {})


# we are passing asset_function as key and then we can render the value of the key on the html page


def profileview(request):
    # context = {
    # }
    return render(request, "profile.html", {})


# we are passing asset_function as key and then we can render the value of the key on the html page


def about_rewardview(request):
    return render(request, "about_reward.html", {})


def blind_rewardview(request):
    return render(request, "blindreward.html", {})


def flexible_workview(request):
    return render(request, "flexible_work.html", {})


def benefitsview(request):
    return render(request, "benefits.html", {})



def searchposts(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(region__icontains=query) | Q(asset_function__icontains=query)

            results = Rem.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'search_page.html', context)

        else:
            return render(request, 'search_page.html')

    else:
        return render(request, 'search_page.html')


def is_valid_queryparam(param):
    return param != '' and param is not None and param !="Choose..."


def filter(request):
    qs = Rem.objects.all()
    region = request.GET.get('region')
    asset_Func = request.GET.get('asset_Func')
    grade = request.GET.get('grade')
    jobFamily = request.GET.get('jobFamily')


    if is_valid_queryparam(region):
        qs = qs.filter(region=region)

    if is_valid_queryparam(asset_Func):
        qs = qs.filter(asset_Func=asset_Func)

    if is_valid_queryparam(grade):
        qs = qs.filter(grade=grade)

    if is_valid_queryparam(jobFamily):
        qs = qs.filter(jobFamily=jobFamily)



    return qs


# def compa_ratio(proposed_Salary, midpoint):
#     proposed_Salary = int('proposed_Salary')
#     midpoint = 100000
#     # midpoint = request.GET.get('midpoint')
#     if midpoint is not None:
#
#         compa = proposed_Salary / midpoint
#     return compa


def BootstrapFilterView(request):
    qs = filter(request)
    proposed_Salary = request.GET.get('proposed_Salary')
    salary_proposed = request.GET.get('one')
    compa = salary_proposed
    STI = request.GET.get('STI')
    proposed_Date = request.GET.get('proposed_Date')

    context = {
        'queryset': qs,
        'categories': Rem.objects.all,
        'proposed_Salary': proposed_Salary,
        'salary_proposed': salary_proposed,
        'STI': STI,
        'proposed_Date': proposed_Date,

        # 'compa': compa,
        # 'compa': compa_ratio(request),
    }

    return render(request, "reward_proposal.html", context)





def date_check(request):
    proposed_Date = request.GET.get('proposed_Date')
    cutoff_Date = datetime.datetime(2020, 4, 1)
    # need to not have this hard coded!
    result = cutoff_Date - proposed_Date
    print(result)

    if proposed_Date - cutoff_Date:

        message = False

    else:
        message = True

    return message


def currency_check(request):
    region = request.GET.get('region')

    if region is "MinAus":
        currency = "AUD"

