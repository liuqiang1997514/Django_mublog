from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/', views.home),
    path('article/<article_id>', views.article_show, name='show'),
    path('edit/<article_id>', views.article_edit, name='edit'),
    path('edit_action/', views.edit_action, name='edit_action'),
]