from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from . import serializers, models
from django.dispatch import receiver
from djoser.signals import user_registered

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def check_username(request):
    print(request.data)
    serializer = serializers.CheckUsernameSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({**serializer.data, "message": "Username is available"})


@receiver(user_registered)
def create_profile(sender, user, request, **kwargs):
    print(user)
    models.Profile.objects.create(user=user)

@api_view(["GET"])
def get_profile(request):
    profile = models.Profile.objects.get(user=request.user)
    serializer = serializers.ProfileSerializer(profile)
    return Response(serializer.data)

# class ProfileViewSet(ModelViewSet):
#     serializer_class = serializers.ProfileSerializer
#     queryset = models.Profile.objects.prefetch_related("user").all()
#     http_method_names = ["get", "options"]

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)
