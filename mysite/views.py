# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now().strftime('%Y-%b-%d %H:%M:%S')
    # t = get_template("current_datetime.html")
    # html = t.render(Context({'current_date':now}))
    # return HttpResponse(html)
    context = {'current_date':now}
    return render(request,'dateapp/current_datetime.html',context)

def hours_ahead(request,offset):
    try:
        offset_int = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset_int)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset_int, dt)
    return HttpResponse(html)
