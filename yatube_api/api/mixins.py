from rest_framework import mixins, viewsets


class FollowGetCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    pass
