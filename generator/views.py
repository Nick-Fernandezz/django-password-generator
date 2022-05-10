from django.shortcuts import render
from django.http import HttpResponse
import random


def password(request):

    the_password = ''

    characters = 'abcdefghijklmnopqrstuvwxyz'

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters += 'abcdefghijklmnopqrstuvwxyz'.upper()
    if request.GET.get('numbers'):
        characters += '123456789'
    if request.GET.get('special'):
        characters += '!@#$%&?*&'

    for i in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})

def about(request):
    return render(request, 'generator/about.html')

