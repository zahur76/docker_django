from django.http import JsonResponse


# Create your views here.
def index(request):
    """Test page"""

    return JsonResponse({"status": "ok"})
