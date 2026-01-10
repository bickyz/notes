from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello Test - DAPP2 2219")
