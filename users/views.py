from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerialazer, User


class PostUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class APIUser(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerialazer(users, many-True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerialazer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerialazer(users, many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = UserSerialazer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)