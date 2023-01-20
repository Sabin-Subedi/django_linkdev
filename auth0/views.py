from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from . import serializers

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def check_username(request):
    print(request.data)
    serializer = serializers.CheckUsernameSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    pass


class ProfileViewSet(ModelViewSet):
    pass
