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
        'translation': '',
        'source_lang': 'de',
        'orig': '',
    }
    if form.get('input'):
        t = client.translate(form.get('input'))
        context['translation'] = t['translatedText']
        context['translated'] = True
        context['source_lang'] = t['detectedSourceLanguage']
        context['orig'] = t['input']
    return HttpResponse(template.render(context, request))
