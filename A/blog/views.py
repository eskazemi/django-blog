from django.shortcuts import render,get_object_or_404
from .models import Article
# Create your views here.
def all_articles(request):
    articles=Article.published.all()
    context={
        'all_articles':articles
    }
    return render(request,'blog/all_articles.html',context)

def article_detail(request,id,slug):
    # article=Article.objects.get(id=id,slug=slug)
    article=get_object_or_404(Article,id=id,slug=slug)
    context={
        'article':article
    }
    return render (request,'blog/article_detail.html',context)