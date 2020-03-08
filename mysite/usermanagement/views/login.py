from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework import status, views
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from usermanagement.base_response import HttpSuccessResponse, HttpErrorResponse
from usermanagement.serializers.user import UserTokenSerializer


class LoginView(views.APIView):
    """
    Login view for user authentication
    """
    serializer_class = UserTokenSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')

        user = authenticate(username=email, password=password)

        if not user:
            return HttpErrorResponse(message='Incorrect login credentials',
                                     status=status.HTTP_403_FORBIDDEN)

        user.last_login = datetime.now()
        user.save()
        token, _ = Token.objects.get_or_create(user=user)
        response = self.serializer_class(user, context={'token': token.key})

        return HttpSuccessResponse(data=response.data,
                                   message='Login success!')


class LogoutView(views.APIView):
    """
    Logout view for user
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        Token.objects.get(user=request.user).delete()
        return HttpSuccessResponse(message='Logout success!')
