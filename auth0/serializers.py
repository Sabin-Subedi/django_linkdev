from rest_framework.serializers import ModelSerializer
from .models import Profile, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class ProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = "__all__"


class CheckUsernameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
