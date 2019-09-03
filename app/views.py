from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views as rest_views
from django.urls import reverse_lazy
from rest_framework.response import Response as R
from rest_framework import status
from app.models import Article
from app.serializers import ArticleSerializer

# Create your views here.
class HomeView(rest_views.APIView):
	def get(self, request, *args, **kwargs):
		return R({'message':'Hello World'}, status=status.HTTP_200_OK)

class ArticleView(rest_views.APIView):
	def get(self, request, *args, **kwargs):
		articles= Article.objects.all()
		results = ArticleSerializer.get_objects(articles)

		return R({'articles': results}, status=status.HTTP_200_OK)
		

	def post(self, request):
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			try:
				item = serializer.create()
				return R({'article': item}, status=status.HTTP_200_OK)
			except Exception as e:
				return R({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
			