from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views as rest_views
from django.urls import reverse_lazy
from rest_framework.response import Response as R
from rest_framework import status

# Create your views here.
class HomeView(rest_views.APIView):
	def get(self, request, *args, **kwargs):
		return R({'message':'Hello World'}, status=status.HTTP_200_OK)
