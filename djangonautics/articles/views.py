from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    art = Article.objects .all().order_by("date")
    return render(request,'article/article_list.html',{'article':art})

def article_details(request, slug):
    return HttpResponse()