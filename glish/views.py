from rest_framework.generics import ListAPIView, RetrieveAPIView
from glish.serializers import LevelSerializer, ModuleSerializer, ModuleElementSerializer
from rest_framework.permissions import IsAuthenticated
from glish.models import Level, Module, ModuleElement
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from utils.gemini import GeminiApi
import json


gemini = GeminiApi()

class ListLevelApiView(ListAPIView):
    serializer_class = LevelSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):  
        return Level.objects.all()


class ListModuleApiView(ListAPIView):
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'level'
    
    def get_queryset(self):
        return Module.objects.filter(level=self.kwargs.get('level'))

    

class ListModuleElementApiView(ListAPIView):
    serializer_class = ModuleElementSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'module'
    
    def get_queryset(self):
        return ModuleElement.objects.filter(module=self.kwargs.get('module')).select_related('module') 
    
    
class ModuleElementAPIView(RetrieveAPIView):
    serializer_class = ModuleElementSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    
    def get_queryset(self):
        return ModuleElement.objects.all()
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_lessons(request):
    
    prompt = request.GET.get('prompt')
    if not prompt:
        return JsonResponse({'status': False, 'detail': 'Prompt parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    response = gemini.generate("I am beginner in english, talk me about '"+ prompt +"', give the answer like : Title, sous tile, explication, example. and give it in HTML5 format.")
    
    
    html_response = response.replace('```html', '').replace('```', '')
    
    from bs4 import BeautifulSoup
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_response, 'lxml')

    # Extract the content of the <body> tag
    body_content = soup.body

    # Convert the content of the <body> tag to a string
    body_string = str(body_content)
        

    return JsonResponse({'status': True, "body_content": body_string}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def ask_questions(request):
    
    prompt = request.GET.get('prompt')
    theme = request.GET.get('theme')
    
    if not prompt:
        return JsonResponse({'status': False, 'detail': 'Prompt parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    response = gemini.generate("try to reply to the following questions :  '"+ prompt +"' and relate it to the topics :  '"+theme+"'. Give it in HTML5 format.")
    
    html_response = response.replace('```html', '').replace('```', '')
    
    from bs4 import BeautifulSoup
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_response, 'lxml')

    # Extract the content of the <body> tag
    body_content = soup.body

    # Convert the content of the <body> tag to a string
    body_string = str(body_content)
        

    return JsonResponse({'status': True, "body_content": body_string}, status=status.HTTP_200_OK)
    
