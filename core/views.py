from django.shortcuts import render
from django.http import HttpResponse
from core.forms import BmiForm

# Create your views here.

def greeting_view(request):
    return render(request, "greeting.html")

def goodbye_view(request):
    return HttpResponse("Goodbye Cruel World")

def bmi(request):
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            bmi = weight/height*2
            return render(request, "bmi.html", {"form": form, "bmi": bmi})
    else:
        form = BmiForm()
    return render(request, "bmi.html", {"form": form})
