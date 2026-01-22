from django.shortcuts import render
from core.forms import ApiForm
from rest_framework.decorators import api_view
from core.models import PersonDb
from api.serializer import Serializer



@api_view(["GET","POST"])
def index(request):
    form = ApiForm()
    person = PersonDb.objects.all()
    message = "" 

    if request.method == "POST":
        form = ApiForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data['sensor_data']
            serializer = Serializer(data=data, many=isinstance(data, list))
            if serializer.is_valid():
                serializer.save()
                message = "message saved"
            else:
                message = f"Validation error: {serializer.errors}"


    return render(request, 'index.html', {
        "form":form,
        "persons":person,
        "message":message,
    })
