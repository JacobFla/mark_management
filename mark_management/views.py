# coding=utf-8
from django.shortcuts import render


def index(request):
    #Objekte aus der Datenbank holen, mittelwert berechne siehe Subject.get_average()

    #Formular erstellen

    #Alles in den Kontext einfügen
    context = {}

    return render(request, "mark_management/index.html", context)