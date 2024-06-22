from rest_framework import serializers
from glish.models import Level, Module, ModuleElement

class LevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Level
        fields = '__all__'
        

class ModuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Module
        fields = '__all__'
        

class ModuleElementSerializer(serializers.ModelSerializer):
    
    module = ModuleSerializer(read_only=True)
    
    class Meta:
        model=ModuleElement
        fields = '__all__'
