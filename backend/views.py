from django.http import HttpResponse
from django.template import loader
from google.cloud import translate

# Initialize Google Translate obj.
client = translate.Client(target_language='de')

# Everything is realized in the index view
def index(request):
    template = loader.get_template('index.html')
    # Get POST-Data if available
    form = request.POST
    # Initialize context
    context = {
        'translated': False,
        'translation': '',
        'source_lang': 'de',
        'orig': '',
    }
    # If form is transmitted (POST), translate and fill out context
    if form.get('input'):
        t = client.translate(form.get('input'))
        context['translation'] = t['translatedText']
        context['translated'] = True
        context['source_lang'] = t['detectedSourceLanguage']
        context['orig'] = t['input']
    return HttpResponse(template.render(context, request))
