# from django.template.loader import get_template
# from django.template import Context
from django.http import HttpResponse
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

def display_headers(request):
    # Exploring information coming from HTTPrequest, use requset.META
    # request.META is just a basic Python dictionary,
    # you'll get KeyError exception when accessing key that doesn't exist.
    # Because HTTP headers are external data - submitted by users' browsers
    # headers are never standardized
    # you should always design for META to fail gracefully
    # (i.e. if a particular header is empty or doesn't exist.) 
    # Use a try/except/get() method to handle the case of undefined keys
    values = request.META.items()  # creates a list of key-value tuples from META dict
    values.sort() # sorts list of tuples by first value in tuple (keys)
    html = []
    for k, v in values:
        # creates a html row with 2 columns : Key , Value
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    # creates a html table appending all the rows
    return HttpResponse('<table>%s</table>' % '\n'.join(html))