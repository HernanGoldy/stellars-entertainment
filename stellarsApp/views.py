from django.shortcuts import render, HttpResponse

# -------------- Vistas renderizadas del sitio -------------- #
def home(request):
    return render(request, 'stellarsApp/home.html')

def lounges(request):
    return render(request, 'stellarsApp/lounges.html')

def promotions(request):
    return render(request, 'stellarsApp/promotions.html')

def previews(request):
    film = {
            'title':'Amsterdam',
            'title2': 'Drama / Comedia / +13',
            'description': 'Historia épica de un crimen romántico, acerca de tres íntimos amigos que se ven envueltos en una de las tramas secretas más escandalosas de la historia norteamericana, basada en hechos de ficción. Producida por Arnon Milchan, Matthew Budman, Anthony Katagas, David O. Russell y Christian Bale. Productores ejecutivos: Yariv Milchan, Michael Schaefer, Sam Hanson.',
            'trailer':"https://www.youtube.com/embed/Xp42uIKRJ9c",
            'original': 'Amsterdam',
            'country': 'Estados Unidos',
            'genre': 'Drama - Comedia',
            'year': '2022',
            'direction': 'David O. Russell',
            'cast': 'Christian Bale, Margot Robbie, John David Washington, Chris Rock, Anya Taylor-Joy, Zoe Saldaña, Mike Myers, Michael Shannon, Timothy Olyphant, Andrea Riseborough, Taylor Swift, Matthias Schoenaerts, Alessandro Nivola, Rami Malek, Robert De Niro',
            'duration': '134 min',
            'distribution': 'Disney',
    }
    return render(request,'stellarsApp/previews.html',{'film': film})

def blog(request):
    return render(request, 'stellarsApp/blog.html')

def base(request):
    return render(request, 'stellarsApp/base.html')
