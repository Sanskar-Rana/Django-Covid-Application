from django.shortcuts import render
import requests
import json



url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "ed1bc72dddmsh607ca998fec0229p1d0ba3jsn84b9fde77e24",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)
# Create your views here.

def home(request):

    fresult = int(response['results'])
    if request.method == "POST":

         myList = []
         for x in range(0, fresult):
             myList.append(response['response'][x]['country'])


         selectedcountry = request.POST['selectedcountry']
         
         
         for x in range(0,fresult):
             if selectedcountry==response['response'][x]['country']:
                 new = response['response'][x]['cases']['new']
                 active = response['response'][x]['cases']['active']
                 critical = response['response'][x]['cases']['critical']
                 recovered = response['response'][x]['cases']['recovered']
                 total = response['response'][x]['cases']['total']
                 deaths = int(total) - int(active)-int(recovered)
         context = {'selectedcountry' : selectedcountry,
                    'myList' : myList,
                    'new' : new,  
                    'active' : active,  
                    'critical' : critical,  
                    'recovered' : recovered,
                    'total' : total, 
                    'deaths' : deaths,
                    }
         return render(request,'home.html',context)
   
    fresult = int(response['results'])
    myList = []
    for x in range(0, fresult):
        myList.append(response['response'][x]['country'])
    context = {'myList' : myList}
    return render(request, 'home.html',context)