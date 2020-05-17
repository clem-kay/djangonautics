from django.urls import path
from .import views

app_name = 'articles'

urlpatterns = [
    path('',views.article_list,name="list"),
    path('^(?P<slug>[\W-]+)/$',views.article_details),
]
