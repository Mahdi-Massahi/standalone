from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema

from .models import User
from .serializers import UserSummarySerializer


class UserView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: UserSummarySerializer})
    def get(self, request):
        user: User = request.user
        serializer = UserSummarySerializer(user)
        return Response(serializer.data)
