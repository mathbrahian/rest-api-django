from rest_framework import serializers
from .models import Note

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "description", "created_at", "updated_at"]