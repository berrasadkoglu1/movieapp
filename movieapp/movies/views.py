from django.shortcuts import render
from .models import Movie,Category

data = {
    "kategoriler": Category.objects.all(),
    "filmler": Movie.objects.all()
}

def home(request):
    return render(request,"index.html",data)


def movies(request):
    return render(request,"movies.html",data)

def moviedetails(request,id):
    data= {
        "movie": Movie.objects.get(id=id)
    }
    return render(request,"details.html",data)

def categoryDetails(request,category):
    
    data2= {
        "kategori": category,
         "movies": Movie.objects.filter(film_turu=category)
    }
    return render(request,"category.html",data2)
