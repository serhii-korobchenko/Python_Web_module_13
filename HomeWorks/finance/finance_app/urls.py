from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/', views.category, name='category'),
    path('income/', views.income, name='income'),
    path('spending/', views.spending, name='spending'),
    path('detail_income/<int:income_id>', views.detail_income, name='detail_income'),
    path('detail_spending/<int:spending_id>', views.detail_spending, name='detail_spending'),
    # path('done/<int:note_id>', views.set_done, name='set_done'),
    # path('delete/<int:note_id>', views.delete_note, name='delete_note'),
]