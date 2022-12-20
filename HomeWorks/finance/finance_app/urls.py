from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/', views.category, name='category'),
    path('income/', views.income, name='income'),
    # path('detail/<int:note_id>', views.detail, name='detail'),
    # path('done/<int:note_id>', views.set_done, name='set_done'),
    # path('delete/<int:note_id>', views.delete_note, name='delete_note'),
]