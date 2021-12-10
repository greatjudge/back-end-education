from django.views import View
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth import get_user_model, login
# from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomAuthForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from quiz.decorators import own_login_required

from .serializers import UserSerializer
# Create your views here.


User = get_user_model()


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'form':  CustomAuthForm()})

    def post(self, request):
        form = CustomAuthForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            try:
                form.clean()
            except ValidationError:
                return render(
                    request,
                    'login.html',
                    {'form': form, 'invalid_creds': True}
                )

            login(request, form.get_user())

            return redirect(reverse('index'))

        return render(request, 'login.html', {'form': form})

    def delete(self, request):
        return self.get(request)

    def put(self, request):
        return self.get(request)


class UserList(APIView):
    """
    List all users
    """

    @own_login_required
    def get(self, request, format=None):
        tests = User.objects.all()
        serializer = UserSerializer(tests, many=True)
        return Response(serializer.data)

    @own_login_required
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
        return get_object_or_404(User, pk=pk)

    @own_login_required
    def get(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = UserSerializer(test)
        return Response(serializer.data)

    @own_login_required
    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)