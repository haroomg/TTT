from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api.serializers import UserTokenSerializer 

class Login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        
        login_serializer = self.serializer_class(data= request.data, context= {"request":request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]
            if user.is_active:
                token,creado = Token.objects.get_or_create(user= user)
                user_serializer  = UserTokenSerializer(user)
                if creado:
                    return Response({
                            "token": token.key,
                            "user": user_serializer.data,
                            "message":'Inicio de sesion exitoso.'
                        },status=status.HTTP_201_CREATED)
                else:
                    all_session = Session.objects.filter(expire_date__gte= datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get("_auth_user_id")):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user= user)
                    return Response({
                            "token": token.key,
                            "user": user_serializer.data,
                            "message":'Inicio de sesion exitoso.'
                        },status=status.HTTP_201_CREATED)
            else:
                return Response({"error":"Este usuario no puede iniciar sesion."}, 
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error":"Nombre de usuario o Contraseña incorrecta."},
                            status= status.HTTP_400_BAD_REQUEST)