from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers, serializers, viewsets

from . import views

router = routers.DefaultRouter()

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^home/$', views.HomeView.as_view()),
	url(r'^articles/$', views.ArticleView.as_view()),
]