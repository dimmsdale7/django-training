from rest_framework import serializers
from app.models import User, Article

class ArticleSerializer(serializers.Serializer):
	user_id = serializers.IntegerField(required=True)
	title= serializers.CharField(max_length=128,required=True)
	description=serializers.CharField(max_length=128, allow_blank=True)

	@classmethod
	def get_object(cls, instance):
		return {'user_id':instance.user_id,'title': instance.title, 'description': instance.description}

	@classmethod
	def get_objects(cls, instances):
		items = []
		for item in instances:
			obj = cls.get_object(item)
			items.append(obj)

		return items

	def create(self):
		article = Article(**self.validated_data)
		article.save()

		return self.get_object(article)