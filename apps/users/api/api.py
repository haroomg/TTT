from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(["GET", "POST"])
def UserApiView(request):
    
    if request.method == "GET":
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)
    
    elif request.method == "POST":
        users_serializer = UserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors)

@api_view(["GET"])
def user_detail_view(request, pk=None):
    
    if request.method == "GET":
        pass