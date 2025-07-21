from .models import Post,Comments
from rest_framework import serializers



class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields='__all__'
        read_only_fields=['author'] 


class PostSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'created_at',
            'updated_at',
            'author',
            'is_published',
            'comments' ,
        ]
        read_only_fields=['author']


