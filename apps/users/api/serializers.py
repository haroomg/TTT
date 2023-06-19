from rest_framework import serializers
from apps.users.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "name", "last_name")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validate_data): 
        user = User(**validate_data)
        user.set_password(validate_data["password"])
        user.save()
        return user

    def update(self, instance, validate_data):
        update_data = super().update(instance, validate_data)
        update_data.set_password(validate_data["password"])
        update_data.save()
        return update_data
    
class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = User
        field = "__all__"
        
    # de esta forma podemos elegir los valores que queremos que aparezcan    
    def to_representation(self, instance): 
        return {
            "id": instance["id"],
            "username": instance["username"],
            "email": instance["email"],
            "password": instance["password"]
        }