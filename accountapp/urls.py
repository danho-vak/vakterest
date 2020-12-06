from django.urls import path
import accountapp.views

app_name = 'accountapp'

urlpatterns = [
    path('test/', accountapp.views.test, name='test'),

    path('create/', accountapp.views.AccountCreateView.as_view(), name='create'), # Class Base View를 적을 때 as_view()로
]
