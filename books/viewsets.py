from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for handling CRUD operations on the 'Book' model.

    Attributes:
        queryset (QuerySet): The set of 'Book' objects that the viewset will operate on.
        serializer_class (Serializer): The serializer class used to transform 'Book' objects to/from JSON.
    """

    queryset = Book.objects.all()          # Retrieve all 'Book' objects.
    serializer_class = BookSerializer      # Use the 'BookSerializer' for JSON serialization/deserialization.
