# from django.template.loader import get_template
# from django.template import Context
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from mysite.forms import ContactForm
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

def email_success(request):
    return HttpResponse("Email sent to admin! You will be contacted shortly.")

def contact(request):
    # Check if request method is POST, which is true in a form submission.
    # If so, this will execute the form-processing part of the view.
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # form.is_valid() checks if all required fields in the form is filled.
        if form.is_valid():
            # if form is valid, then clean the form data.
            cd = form.cleaned_data
            # Execute whatever you want to do with the form.
            #################
            # Redirect user to another page
            # You should ALWAYS do a redirect after a POST, 
            # so that the user does not duplicate the POST request
            return HttpResponseRedirect('/contact/thanks/')
    else:
        # Set a pre-populated text in the subject.
        # Note that passing in 'initial' does not cause the form to be bound. (i.e. it is unbound)
        # This means that it won't have any error messages unlike a bound form.
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    context = {'form': form}
    return render(request, 'contact_form/contact_form.html', context)