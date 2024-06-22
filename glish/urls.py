from django.urls import path
from glish.views import ListLevelApiView, ListModuleApiView, ListModuleElementApiView, ModuleElementAPIView


urlpatterns = [
    path('levels', ListLevelApiView.as_view(), name='levels'),
    path('levels/<int:level>/modules', ListModuleApiView.as_view(), name='modules'),
    path('levels/modules/<int:module>/module_elements', ListModuleElementApiView.as_view(), name='module_elements'),
    path('levels/modules/module_elements/<int:id>', ModuleElementAPIView.as_view(), name='module_element_detail'),
]