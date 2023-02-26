from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import *
from .serializer import *

# Create your views here.
@api_view(['GET'])
def get_questions(request):
    serializer = question_serialisers(teacher.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_questions(request):
    serializer = question_serialisers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)