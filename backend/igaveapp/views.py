from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Receipt
from .serializers import UserSerializer, ReceiptSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ReceiptViewSet(viewsets.ModelViewSet):
    serializer_class = ReceiptSerializer

    def get_queryset(self):
        return Receipt.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(["GET"])
def get_users(request):
    users = User.objects.all()

    data = [
        {
            "id": u.id,
            "username": u.username,
            "password": u.password,
            "date_joined": u.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            "is_staff": u.is_staff,
        }
        for u in users
    ]

    return JsonResponse(data, safe=False)


@csrf_exempt
@api_view(["DELETE"])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    user.delete()
    return JsonResponse({"message": "User deleted"})


@csrf_exempt
@api_view(["POST"])
def register_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "User already exists"}, status=400)

    User.objects.create_user(username=username, password=password)
    return JsonResponse({"success": True})


@csrf_exempt
@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return JsonResponse(
            {"success": False, "error": "Invalid credentials"},
            status=400,
        )

    return JsonResponse(
        {
            "success": True,
            "username": user.username,
            "is_staff": user.is_staff,
        }
    )
