from rest_framework.response import Response
from .models import Post,Comments
from .serializers import PostSerializer,CommentsSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)