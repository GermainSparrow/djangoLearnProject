from django.http import HttpResponse

def demo01 (request):
    html  = '<h1> hello world </h1>'
    return HttpResponse(html)
