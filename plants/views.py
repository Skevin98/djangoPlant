
from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.loader import get_template
import requests
from plants.datatest import dataset, firstThreeFlowers
api_key = "BHZ6vXLWZhSu681vE647FyCh8hb2VieY8sTervUb91LT-wJymtVQUqkqyiFp5owI"


def index(request):
    """Vue affichant la page d'accueil"""
    # print("+++++ : ",request.GET.get('queue', 'pas de queue'))
    # if 'queue' not in request.GET or request.GET['queue'] == '':
    #     queue = 'red'
    # else:
    #     queue = request.GET['queue']
         
    # try:
    #     response = requests.get("https://api.floracodex.com/v1/plants?key=%s&q=%s"%(api_key, queue))
        
    # except:
    #     pass
    # else:
    #     responseJSON = response.json()
    #     pprint(responseJSON)
    #     plants = responseJSON['data'][:10]
    #     print("######## queue : ", queue)
    #     #pprint(plants)
    #     return render(request, 'base.html',{'plants':plants})
    plants = dataset['data']
    return render(request, 'base.html',{'plants': enumerate(plants)})
    
    
def ajax_index(request):
    """requete ajax permettant de faire une nouvelle recherche sans actualiser la page"""
    # print("+++++ in ajax : ",request.GET.get('queue', 'pas de queue'))
    # if 'queue' not in request.GET or request.GET['queue'] == '':
    #     queue = 'red'
    # else:
    #     queue = request.GET['queue']
         
    # try:
    #     response = requests.get("https://api.floracodex.com/v1/plants?key=%s&q=%s"%(api_key, queue))
        
    # except:
    #     pass
    # else:
    #     responseJSON = response.json()
    #     pprint(responseJSON)
    #     plants = responseJSON['data'][:10]

    #     return render(request,'query.html',{'plants':plants})
    pass



def detail(request, id):
    """Retourne la vue affichant les details d'une fleur selectionnée dans la liste"""
    if id != None:
        #flower contient les infos de la fleur numero id. 
        flower = firstThreeFlowers[id]
        
        
        #++++++++++++++        Travail à Faire         +++++++++++++++++++++++++++++++++
        
        
        # retourner un render qui affichera le template detail.html avec les données de flower
        # Les données des 3 premieres fleurs sont disponibles dans datatest.py
        
        #voir la fonction index comme exemple 
        return render(request,'detail.html',{'flower':flower}) #Effacer ce return et ecrire le votre
        
# Create your views here.
 