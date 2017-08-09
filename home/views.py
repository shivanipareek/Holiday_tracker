from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from models import UserProfile
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from login.serializers import UserProfileSerializer
from rest_framework.response import Response

class Homeview(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home/home.html'

    def get(self, request):
        args = UserProfile.objects.all()
        serializer = UserProfileSerializer(args, many=True)
        return Response({'user': request.user})

'''
def profile(request):
    args = {'user': request.user}
    return render(request,'home/home.html',args)'''