from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'eth-utils', 'url': 'http://pypi.python.org/pypi/eth-utils/0.7.4'},
	{'name':'djangorestframework', 'url': 'http://pypi.python.org/pypi/djangorestframework/3.7.7'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
