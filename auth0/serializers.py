from rest_framework.serializers import ModelSerializer
from .models import Profile, User


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class CheckUsernameSerializer(ModelSerializer):
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)

    class Meta:
        model = User
        fields = ["username"]
