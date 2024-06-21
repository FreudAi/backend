from rest_framework.generics import ListAPIView
from glish.serializers import LevelSerializer, ModuleSerializer, ModuleElementSerializer
from rest_framework.permissions import IsAuthenticated
from glish.models import Level, Module, ModuleElement

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
        return ModuleElement.objects.filter(module=self.kwargs.get('module'))

