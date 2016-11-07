from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib import messages
from syerch.settings import CLIENT_ID, CLIENT_SECRET
from forms import SearchForm
import json
from django.template import loader

# Create your views here.


def index(request):
    if request.method == 'POST':
        client_id = CLIENT_ID
        client_secret = CLIENT_SECRET
        host = HOST
        r = requests.post('https://api.yelp.com/oauth2/token',
		          data={'client_id': client_id,     
                                'grant_type': 'password',   
                                'client_secret': client_secret})
        if not r.ok:
            form = SearchForm()
            messages.error(request, 'Authentication Failure.')
            return render(request, 'index.html', {'form': form})

        r_data = r.json()
        token = r_data.get('access_token')
        token_type = r_data.get('token_type')

        form = SearchForm(request.POST)
        print request.POST
        if form.is_valid():
            city = 'Atlanta'
            print city
            payload = {'term': form.data.get('search'),
                       'location': city}
            header = {'Authorization': token_type + ' ' + token,
                      'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.get(
                    'https://api.yelp.com/v3/businesses/search',
                    headers=header,
                    params=payload)
            print response.json()
            return render(request, 'results.html',
                          {'data': response.json().get('businesses')})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
    
    return render(request, 'index.html', {'form': form})
