from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    # pk_f012f44498454daeabdf70e2c2a2edac
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_f012f44498454daeabdf70e2c2a2edac")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."


    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})