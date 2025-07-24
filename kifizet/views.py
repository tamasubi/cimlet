from django.shortcuts import render

import random

#osszeg = int(input("Írj be egy összeget: "))

def bontsd_random_cimletekre(osszeg):
    cimeletek = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5]
    felbontas = {}

    while osszeg >= 5:
        lehetseges = [c for c in cimeletek if c <= osszeg]
        if not lehetseges:
            print("nem lehetséges")
            break
        cimlet = random.choice(lehetseges)
        max_db = osszeg // cimlet
        random_db = random.randint(1, max_db)
        felbontas[cimlet] = felbontas.get(cimlet, 0) + random_db
        osszeg -= cimlet * random_db
       

    return felbontas



#v = bontsd_random_cimletekre(osszeg)

#print(v)

def penz_view(request):
    eredmeny = {}
    if request.method == "POST":
        try:
            osszeg = int(request.POST.get("osszeg", 0))
            eredmeny = bontsd_random_cimletekre(osszeg)
        except ValueError:
            eredmeny = {"Hiba": "Érvénytelen összeg"}

    return render(request, "felbontas.html", {"eredmeny": eredmeny})

