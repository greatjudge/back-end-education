from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
# Create your views here.


User = get_user_model()


class UserList(APIView):
    """
    List all users
    """
    def get(self, request, format=None):
        tests = User.objects.all()
        serializer = UserSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = UserSerializer(test)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)