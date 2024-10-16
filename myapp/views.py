from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def home_view(request):
    return Response({"message": "Hello, we are dockerizing Django!"})