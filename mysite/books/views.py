# Create your views here.
from django.http        import HttpResponse
from django.shortcuts   import render_to_response
from forms              import ContactForm

def hello(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    ua = request.META.get('HTTP_USER_AGENT', 'unknow')
    return HttpResponse("page %s, is_secure: %s, ua: [%s], <table>%s</table>" % \
            (request.path, request.is_secure(), ua, '\n'.join(html)))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm
    return render_to_response('contact_form.html', {'form': form})
