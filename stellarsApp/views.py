from django.shortcuts import render, HttpResponse

# -------------- Vistas renderizadas del sitio -------------- #
def home(request):
    return render(request, 'stellarsApp/home.html')

def lounges(request):
    return render(request, 'stellarsApp/lounges.html')

def promotions(request):
    return render(request, 'stellarsApp/promotions.html')

def previews(request):
    return render(request, 'stellarsApp/previews.html')

def blog(request):
    return render(request, 'stellarsApp/blog.html')

def base(request):
    return render(request, 'stellarsApp/base.html')
