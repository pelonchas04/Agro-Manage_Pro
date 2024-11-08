from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserListSerializer, UserModifySerializer
from apps.users.models import User

class UserAPI(APIView):

    def get(self, request):
        # if pk != None:
        #     user = User.objects.filter(id = pk).first()
        #
        #     if user == None:
        #         return Response(data={"error": "No se ha encontrado un usuario con este id"}, status=status.HTTP_404_NOT_FOUND)
        #
        #     user_serializer = UserSerializer(user)
        #     return Response(data={"Usuario": user_serializer.data}, status=status.HTTP_200_OK)

        users = User.objects.all().values('id', 'password', 'username', 'name', 'last_name', 'is_active', 'tel', 'observations', 'change_password', 'change_password_next_session')
        users_serializer = UserListSerializer(users, many=True)
        return Response(data={"Usuarios": users_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        user_request = UserModifySerializer(data = request.data, context=request.data)
        if (user_request.is_valid()):
            user_request.save()
            return Response(data={"mensaje": "Usuario creado correctamente"}, status = status.HTTP_201_CREATED)

        return Response(data={"error": user_request.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        user = User.objects.filter(id = pk).first()

        if user != None:
            user_request = UserModifySerializer(user, data = request.data)
            if user_request.is_valid():
                user_request.save()
                return Response(data={"mensaje": "Usuario actualizado"}, status= status.HTTP_200_OK)

            return Response(data={"error": user_request.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={"error": "Usuario no encontrado"}, status= status.HTTP_404_NOT_FOUND)