from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def test(request):
    return render(request, 'accountapp/test.html')


# 1. sign up
# 2. sign in
# 3. view info
# 4. change info
# 5. quit


class AccountCreateView(CreateView): # generic view를 상속
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:test') # class형 view에서 사용하는 reverse()
    template_name = 'accountapp/create.html'
