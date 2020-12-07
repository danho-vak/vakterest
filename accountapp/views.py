from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .decorators import account_ownership_required
from .forms import AccountUpdateForm


has_ownership = [account_ownership_required, login_required]  # List for method_decorator


@login_required
def test(request):
        return render(request, 'accountapp/test.html')


# Class Based Views
class AccountCreateView(CreateView): # generic view를 상속
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:test') # class형 view에서 사용하는 reverse()
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView): # generic view를 상속
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:test') # class형 view에서 사용하는 reverse()
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'