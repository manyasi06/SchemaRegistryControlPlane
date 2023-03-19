from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('',views.index,name='index')
    path('schemas/',views.SchemaList.as_view()),
    path('schemas/<int:pk>',views.SchemaDetail.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)