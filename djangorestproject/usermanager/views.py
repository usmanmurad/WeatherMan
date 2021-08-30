from usermanager.models import User
from rest_framework import viewsets, status
from usermanager.serializers import UserSerializer, CreateUserSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'Success'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
