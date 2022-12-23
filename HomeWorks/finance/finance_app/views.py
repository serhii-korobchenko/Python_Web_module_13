from django.shortcuts import render, redirect
from .models  import Category, Income, Spending, IncomeToCategory, SpendingToCategory


# Create your views here.
def main(request):
    incomes = Income.objects.all()
    spendings = Spending.objects.all()
    categories = Category.objects.all()
    return render(request, 'finance_app/index.html', {"incomes": incomes, "spendings": spendings, "categories": categories})

def category(request):
    if request.method == 'POST':
        name = request.POST['name']
        if name:
            tl = Category(name=name)
            tl.save()
        return redirect(to='/')
    return render(request, 'finance_app/category.html', {})

def income (request):
    if request.method == 'POST':
        summa = request.POST['summa']
        transaction_date = request.POST['transaction_date']
        list_categories = request.POST.getlist('categories')
        if summa and transaction_date:
            categories = Category.objects.filter(name__in=list_categories)
            income = Income.objects.create(summa=summa, transaction_date=transaction_date, )
            for category in categories.iterator():
                income.categories.add(category)
                income.save()
        return redirect(to='/')

    categories = Category.objects.all()
    return render(request, 'finance_app/income.html', {"categories": categories})

def spending (request):
    if request.method == 'POST':
        summa = request.POST['summa']
        transaction_date = request.POST['transaction_date']
        list_categories = request.POST.getlist('categories')
        if summa and transaction_date:
            categories = Category.objects.filter(name__in=list_categories)
            spending = Spending.objects.create(summa=summa, transaction_date=transaction_date,)
            for category in categories.iterator():
                spending.categories.add(category)
                spending.save()
        return redirect(to='/')

    categories = Category.objects.all()
    return render(request, 'finance_app/spending.html', {"categories": categories})

def detail_income(request, income_id):
    income = Income.objects.get(pk=income_id)
    income.category_list = ', '.join([str(name) for name in income.categories.all()])

    return render(request, 'finance_app/detail_income.html', {"income": income,  })


def detail_spending(request, spending_id):
    spending = Spending.objects.get(pk=spending_id)
    spending.category_list = ', '.join([str(name) for name in spending.categories.all()])

    return render(request, 'finance_app/detail_spending.html', {"spending": spending,  })

def detail_category(request, category_id):
    category = Category.objects.get(pk=category_id)

    return render(request, 'finance_app/detail_category.html', {"category": category,  })

def delete_income(request, income_id):
    income = Income.objects.get(pk=income_id)
    income.delete()
    return redirect(to='/')

def delete_spending(request, spending_id):
    spending = Spending.objects.get(pk=spending_id)
    spending.delete()
    return redirect(to='/')

def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect(to='/')

def report (request):

    if request.method == 'POST':
        sum_income = 0
        sum_spending = 0
        low_limit = request.POST['low_limit']
        up_limit = request.POST['up_limit']

        incomes_for_report = Income.objects.exclude(transaction_date__lt=low_limit).exclude(transaction_date__gt=up_limit)
        spendings_for_report = Spending.objects.exclude(transaction_date__lt=low_limit).exclude(transaction_date__gt=up_limit)

        for item in incomes_for_report:
            sum_income = sum_income + item.summa

        for item in spendings_for_report:
            sum_spending = sum_spending + item.summa


        return render(request, 'finance_app/report.html',{"incomes_for_report": incomes_for_report, "spendings_for_report": spendings_for_report, \
                                                          "sum_income": sum_income,"sum_spending": sum_spending,})


    return render(request, 'finance_app/report.html', {})