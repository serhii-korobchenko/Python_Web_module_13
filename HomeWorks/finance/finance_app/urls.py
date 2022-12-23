from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/', views.category, name='category'),
    path('income/', views.income, name='income'),
    path('spending/', views.spending, name='spending'),
    path('report/', views.report, name='report'),
    path('detail_income/<int:income_id>', views.detail_income, name='detail_income'),
    path('detail_spending/<int:spending_id>', views.detail_spending, name='detail_spending'),
    path('detail_category/<int:category_id>', views.detail_category, name='detail_category'),
    path('delete_spending/<int:spending_id>', views.delete_spending, name='delete_spending'),
    path('delete_category/<int:category_id>', views.delete_category, name='delete_category'),
    path('delete/<int:income_id>', views.delete_income, name='delete_income'),

]