from django.db import models


class Level(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    min_point = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super(Level, self).save(*args, **kwargs)
        return self
    
    def __str__(self) -> str:
        return self.name
    
    
class Module(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    level = models.ForeignKey(to=Level, related_name='modules', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        super(Module, self).save(*args, **kwargs)
        return self
    
    def __str__(self) -> str:
        return self.name
    
class ModuleElement(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    module = models.ForeignKey(to=Module, related_name='elements', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
