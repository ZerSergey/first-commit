from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def reverse(request):
    text = request.GET['study_text']
    number_text = len(text.split())
    reverse_text = text[::-1]
    return render(request, "reverse.html", {"study_text": text, "numbertext": number_text, "reversetext": reverse_text})