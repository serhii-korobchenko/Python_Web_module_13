from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/', views.category, name='category'),
    path('income/', views.income, name='income'),
    path('spending/', views.spending, name='spending'),
    path('detail_income/<int:income_id>', views.detail_income, name='detail_income'),
    path('detail_spending/<int:spending_id>', views.detail_spending, name='detail_spending'),
    path('delete_spending/<int:spending_id>', views.delete_spending, name='delete_spending'),
    path('delete/<int:income_id>', views.delete_income, name='delete_income'),

]