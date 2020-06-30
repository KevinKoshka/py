from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view())
]

# incluir format_suffix_patterns es opcional. Permite a nuestra API manejar
# los formatos del archivo para el endpoint dado, por ejemplo: http://example.com/api/items/4.json
# sería lo mismo que http://example.com/api/items/4
urlpatterns = format_suffix_patterns(urlpatterns)
