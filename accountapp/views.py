from django.shortcuts import render


def test(request):
    return render(request, 'accountapp/temp.html')
