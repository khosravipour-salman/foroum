from rest_framework import serializers
from foroum.models import (
    Room, Post, Like, Comment
)
from accounting.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=True, read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = [
            'title',
            'profile_image',
            'owner',
            'members',
            'bio',
            'create', 
        ]


class PostSerializer(serializers.ModelSerializer):
    room = RoomSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image', 'room', 'create', ]


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    post = PostSerializer(many=False, read_only=True)

    class Meta:
        model = Like
        fields = ['user', 'post', 'vote', ]


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    post = PostSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = ['user', 'post', 'text', ]
