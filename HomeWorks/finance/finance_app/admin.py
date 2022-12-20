from django.contrib import admin
from .models  import Category, Income, Spending, IncomeToCategory, SpendingToCategory


# Register your models here.
admin.site.register(Category)
admin.site.register(Income)
admin.site.register(Spending)
admin.site.register(IncomeToCategory)
admin.site.register(SpendingToCategory)