from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Receipt
from .serializers import UserSerializer, ReceiptSerializer

from rest_framework.permissions import AllowAny

import json





class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    


class ReceiptViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing receipts.
    """
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return receipts for the current user only."""
        return Receipt.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Set the user to the current user when creating a receipt."""
        serializer.save(user=self.request.user)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@api_view(["GET"])
@permission_classes([AllowAny])
def get_users(request):
    users = User.objects.all()

    data = []
    for u in users:
        data.append({
            "id": u.id,
            "username": u.username,
            "password": u.password,
            "date_joined": u.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
            "is_staff": u.is_staff,
        })

    return JsonResponse(data, safe=False)


@csrf_exempt
def delete_user(request, id):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse({"message": "User deleted"}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

@csrf_exempt
def register_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    data = json.loads(request.body)

    username = data.get("username")
    password = data.get("password")

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "User already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return JsonResponse({"success": True, "message": "User created"})
    

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            return JsonResponse({
                "success": True,
                "message": "Login successful",
                "username": user.username,
                "is_staff": user.is_staff,
            })
        else:
            return JsonResponse({"success": False, "error": "Invalid credentials"}, status=400)

