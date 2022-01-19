from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person


def index(request):
    context = {"status": "first"}
    try:
        if request.session['person']:
            people = request.session['person']
            context = {"name": people["name"], "surname": people["surname"], "status": people["status"]}
        return render(request, "form/index.html", context)
    except BaseException:
        return render(request, "form/index.html", context)


def create(request):
    people, created = Person.objects.get_or_create(name=request.POST.get("name"), surname=request.POST.get("surname"),
                                                   email=request.POST.get("email"))

    request.session['person'] = {"name": request.POST.get("name"), "surname": request.POST.get("surname"),
                                 "status": created}

    return HttpResponseRedirect('/')


def name_list(request):
    people = Person.objects.all()
    return render(request, 'form/name_list.html', {"people": people})
