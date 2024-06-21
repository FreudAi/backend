from django.db import models


class Level(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    desc = models.TextField()
    min_point = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
    
class Module(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    desc = models.TextField()
    level = models.ForeignKey(to=Level, related_name='modules', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
class ModuleElement(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    desc = models.TextField()
    module = models.ForeignKey(to=Module, related_name='elements', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
