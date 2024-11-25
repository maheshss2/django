from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Define root_view inline
def root_view(request):
    return JsonResponse({"message": "Welcome to the API"}, status=200)

urlpatterns = [
    path('', root_view, name='root'),  # Map the root URL
    path('admin/', admin.site.urls),
    path('auth/', include('user_management.urls')),  # Include URLs from user_management app
]
