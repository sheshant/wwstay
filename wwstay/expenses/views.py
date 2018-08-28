from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.template.loader import render_to_string

from expenses.forms import ImageUploadForm
from .models import Expense
from .forms import ExpenseForm


def expense_list(request):
    expenses = Expense.objects.all()
    sort = request.GET.get('sort')
    if sort:
        expenses = expenses.order_by(sort)
    total_expense = expenses.aggregate(Sum('price')).get('price__sum').__str__()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total_expense': total_expense})


def save_expense_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            data['form_is_valid'] = True
            expenses = Expense.objects.all()
            data['html_expense_list'] = render_to_string('expenses/includes/partial_expense_list.html', {
                'expenses': expenses
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def expense_create(request):
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = ExpenseForm(request.POST, request.FILES)
    else:
        form = ExpenseForm()
    return save_expense_form(request, form, 'expenses/includes/partial_expense_create.html')


def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
    else:
        form = ExpenseForm(instance=expense)
    return save_expense_form(request, form, 'expenses/includes/partial_expense_update.html')


def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    data = dict()
    if request.method == 'POST':
        expense.delete()
        data['form_is_valid'] = True
        expenses = Expense.objects.all()
        data['html_expense_list'] = render_to_string('expenses/includes/partial_expense_list.html', {
            'expenses': expenses
        })
    else:
        context = {'expense': expense}
        data['html_form'] = render_to_string('expenses/includes/partial_expense_delete.html', context, request=request)
    return JsonResponse(data)


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['image'])
            # form.save()
            return redirect('expenses:home')
    else:
        form = ImageUploadForm()
    return render(request, 'expenses/model_form_upload.html', {
        'form': form
    })
