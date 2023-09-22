from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .mixins import FollowGetCreateViewSet
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        return serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        )


class FollowViewSet(FollowGetCreateViewSet):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly,)
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, )
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
