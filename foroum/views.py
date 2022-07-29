from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from foroum.models import Room, Post, Comment, Like
from foroum.serializers import (
	RoomSerializer, PostSerializer, CommentSerializer, LikeSerializer
)


class RoomListView(generics.ListAPIView):
	# per-view permissions or global dakhele settings.py
	# AllowAny -- IsAuthenticated -- IsAuthenticatedOrReadOnly -- DjangoModelPermissions and DjangoObjectPermissions
	# Ifunauthenticated
	# 	HTTP 401 : Unauthorized
	#   HTTP 403 : Permission denied
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class RoomDetailView(generics.RetrieveAPIView):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Room.objects.all()
	serializer_class = RoomSerializer


class PostListView(generics.ListAPIView):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetailView(generics.RetrieveAPIView):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer


# class Post()