from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'translated': False,
    }
    return HttpResponse(template.render(context, request))
