from django.shortcuts import render
from .models import ShortURl
import random, string
from datetime import datetime
from .forms import CreateNewShortURL

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
def createShortURL(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_URL']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURl.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = ShortURl(original_URL=original_website, short_url=random_chars, time_date_created=d)
            s.save()
            return render(request, 'urlcreated.html', {'chars':random_chars})
    
    else:
        form=CreateNewShortURL()
        context={'form': form}
        return render(request, 'create.html', context)
def redirect(request, url):
    current_obj = ShortURl.objects.filter(short_url = url)
    if len(current_obj) == 0:
        return render(request, 'pagenotfound.html')
    context = {'obj':current_obj[0]}
    return render(request, 'redirect.html')
