from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# JWT simple token serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["message"] = "Welcome to ShopNext"

        return token