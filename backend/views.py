from django.http import HttpResponse
from django.template import loader
from google.cloud import translate

client = translate.Client(target_language='de')

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    form = request.POST
    context = {
        'translated': False,
        'translation': 'Test-Übersetzung',
    }
    if form.get('input'):
        # ToDo: Translate-
        context['translation'] = form.get('input')
        context['translated'] = True
    return HttpResponse(template.render(context, request))
