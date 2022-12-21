from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)


    def __str__(self):
        return self.name


class Income(models.Model):
    summa = models.FloatField(max_length=50)
    transaction_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='IncomeToCategory')


    def __str__(self):
        return str(self.summa)

class Spending(models.Model):
    summa = models.FloatField(max_length=50)
    transaction_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='SpendingToCategory')

    def __str__(self):
        return str(self.summa)


class IncomeToCategory(models.Model):
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class SpendingToCategory(models.Model):
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)