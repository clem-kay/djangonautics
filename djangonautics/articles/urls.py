from django.urls import path
from .import views

urlpatterns = [
    path('',views.article_list),
    path('^(?P<slug>[\W-]+)/$',views.article_details),
]
