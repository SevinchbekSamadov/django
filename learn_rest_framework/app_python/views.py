from django.shortcuts import render
from rest_framework.views import APIView
from .models import Pupils
from rest_framework.views import Response
from django.forms import model_to_dict

# Create your views here.


class PupilsView(APIView):
    def get(self, request):
        pupils = Pupils.objects.all().values()
        return Response({'ouoils:': list(pupils)})
    
    def post(self,request):
        new_pupil =Pupils.objects.create(
            first_name =  request.data['first_name'],
            last_name =  request.data['last_name'],
            exam_mark = request.data['exam_marke'],
        )
        return Response({'new_pupil': model_to_dict(new_pupil)}) #json ga ogiradi model_to_dict <- mana shu     