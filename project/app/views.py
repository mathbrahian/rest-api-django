from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Note
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NoteSerializers


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializers

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def note(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializers(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        new_note = JSONParser().parse(request)
        serializer = NoteSerializers(data=new_note)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def note_id(request, id):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoteSerializers(note)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        note_data = JSONParser().parse(request)
        serializer = NoteSerializers(note, data=note_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        note.delete()
        return HttpResponse(status=204)

    