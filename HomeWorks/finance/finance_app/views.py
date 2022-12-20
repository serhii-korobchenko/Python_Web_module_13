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
        list_categories = request.POST.getlist('catigories')
        if summa and transaction_date:
            categories = Category.objects.filter(name__in=list_categories)
            income = Income.objects.create(summa=summa, transaction_date=transaction_date,)
            for category in categories.iterator():
                income.categories.add(category)
        return redirect(to='/')

    categories = Category.objects.all()
    return render(request, 'finance_app/income.html', {"categories": categories})

# def detail(request, note_id):
#     note = Note.objects.get(pk=note_id)
#     note.tag_list = ', '.join([str(name) for name in note.tags.all()])
#     return render(request, 'finance_app/detail.html', {"note": note})
#
#
# def set_done(request, note_id):
#     Note.objects.filter(pk=note_id).update(done=True)
#     return redirect(to='/')
#
#
# def delete_note(request, note_id):
#     note = Note.objects.get(pk=note_id)
#     note.delete()
#     return redirect(to='/')
