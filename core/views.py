from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils import translation



def home(request):
    context = {
        'hello' : _('hello')
    }
    return render(request, 'core/index.html', context)


def user_setting(request):
    return render(request, "core/user_settings.html")

