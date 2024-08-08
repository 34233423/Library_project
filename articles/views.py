# articles/views.py
from articles.models import Article
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/search/')
        else:
            return render(request, 'articles/login.html', {'error': 'Invalid username or password'})
    return render(request, 'articles/login.html')

@login_required
def home(request):
    return render(request, 'articles/home.html')

@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        results = Article.objects.filter(content__icontains=query)
    else:
        results = Article.objects.none()
    return render(request, 'articles/search.html', {'results': results})

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})
