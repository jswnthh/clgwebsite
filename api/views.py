from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import PersonDb
from .serializer import Serializer

@api_view(['GET'])
def getData(request):
    persons = PersonDb.objects.order_by("-created_at")
    serializer = Serializer(persons, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    serializer = Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()



