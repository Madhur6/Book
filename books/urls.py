from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BookViewSet

# Create a DefaultRouter instance for handling CRUD operations on 'books'.
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Include the automatically generated URL patterns from the router in the urlpatterns.
urlpatterns = [
    path('', include(router.urls))  # Include CRUD endpoints for 'books'.
]
