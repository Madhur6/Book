from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the 'Book' model.

    Attributes:
        model (Model): The 'Book' model that the serializer is based on.
        fields (list): The fields to include in the serialized representation.
        read_only_fields (list): The fields that should be read-only in the serialized representation.
    """

    class Meta:
        model = Book                           # Use the 'Book' model for serialization.
        fields = ["id", "title", "price", "created", "updated"]  # Include these fields in the serialized representation.
        read_only_fields = ["id", "created", "updated"]          # Specify read-only fields in the serialized representation.
