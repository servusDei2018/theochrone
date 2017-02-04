from django.shortcuts import render
import subprocess
import os
import sys
import pickle
from .forms import * 

#os.chdir('../..')
os.chdir("/home/partage/.scripts/projet_liturgie/wip_fetes/programme")
sys.path.append('.')
import adjutoria
import officia
# Create your views here.

def home(request):
    """A function which defines homepage"""
    recherche_simple = RechercheSimple(request.GET or None)
    recherche_mot_clef = RechercheMotClef(request.GET or None)
    date = None
    mots_clefs = ''
    if recherche_simple.is_valid():
        date = recherche_simple.cleaned_data['date_seule']
    if recherche_mot_clef.is_valid():
        mots_clefs = recherche_mot_clef.cleaned_data['recherche']
        plus = recherche_mot_clef.cleaned_data['plus']
        try:
            annee = int(recherche_mot_clef.cleaned_data['annee'])
        except TypeError:
            annee = adjutoria.datetime.date.today().year
    if not date:
        date = adjutoria.datetime.date.today() 

    with open('./data/samedi.pic','rb') as file:
        pic=pickle.Unpickler(file)
        samedi=pic.load()
    
    retour = ''
    if mots_clefs == '':
        Annee = officia.fabrique_an(date,date)
        try:
            Annee[date]
        except KeyError:
            Annee[date] = []
        liste = adjutoria.selection(Annee[date],date,Annee,samedi)
        titre=date
        inversion=False
    else:
        liste = officia.inversons(mots_clefs,adjutoria.datetime.date(annee,1,1),adjutoria.datetime.date(annee,12,31),samedi,exit=False,plus=plus)
        titre = mots_clefs
        inversion=True

    return render(request,'kalendarium/accueil.html',locals())
