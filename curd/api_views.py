from . import serializers,models
from rest_framework import viewsets

class FriendViewset(viewsets.ModelViewSet):
    queryset=models.Friend.objects.all()
    serializer_class=serializers.FriendSerializer

class BelongingViewset(viewsets.ModelViewSet):
    queryset=models.Belonging.objects.all()
    serializer_class=serializers.BelongingSerializer

class BorrowedViewset(viewsets.ModelViewSet):
    queryset=models.Borrowed.objects.all()
    serializer_class = serializers.BorrowedSerializer