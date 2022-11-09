from django.shortcuts import render
import requests
# Create your views here.

def home(request):
    if request.method=='POST':
        city = request.POST.get('city')
        res  = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b5a0ca7cc552258f6947837419a97ae7') 
        python_data = res.json()
        if python_data['cod']==200:
            data = {
                'country_code':str(python_data['sys']['country']),
                'coord':str(python_data['coord']['lon']) + ' ' +str(python_data['coord']['lat']),
                'temp':str(python_data['main']['temp'])+'k',
                'pressure':str(python_data['main']['pressure']),
                'humidity':str(python_data['main']['humidity']),
            }
        else:
            data = {
                'error':'invalid search'
            }
    else:
        city = ""
        data = {}
    return render(request,'home.html',{'city':city,'data':data})