from django.urls import path
from glish.views import ListLevelApiView, ListModuleApiView, ListModuleElementApiView


urlpatterns = [
    path('levels', ListLevelApiView.as_view(), name='levels'),
    path('modules/<int:level>', ListModuleApiView.as_view(), name='modules'),
    path('module_elements/<int:module>', ListModuleElementApiView.as_view(), name='module_elements'),
]