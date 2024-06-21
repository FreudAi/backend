"""
URL configuration for zahageek_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from glish.models import Level, Module, ModuleElement

def create_super_user(request):
    from authentication.models import User
    User.objects.create_superuser(email="admin@admin.com", password="admin123##", is_staff=True, is_superuser=True)
    return HttpResponse("Admin created successfully!")

def import_data(request):
    import json
    with open('levels.json', 'r') as f:
        data_string = f.read()

    data = json.loads(data_string)
    
    level_order = 1
    min_point = 0
    for level in data['levels']:
        l = Level(order=level_order, name=level['name'], desc=level['desc'], min_point=min_point)
        saved_l = l.save()
        
        module_order = 1
        for module in level['modules']:
            m = Module(order=module_order, name=module['name'], desc=module['desc'], level=saved_l)
            saved_m = m.save()
            
            module_element_order = 1    
            for element in module['module_elements']:
                e = ModuleElement(order=module_order, name=element['name'], desc=element['desc'], module=saved_m)
                e.save()
                module_element_order += 1
            
            module_order += 1
        
        level_order += 1
        min_point += 300
        
    
    return HttpResponse("Data imported successfully!")

urlpatterns = [
    path('create-super-user', create_super_user, name='create-super-user'),
    path('import-data', import_data, name='import-data'),
    path('admin/', admin.site.urls),
    #path('accounts/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('authentication.urls')),
    path('api/glish/', include('glish.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
