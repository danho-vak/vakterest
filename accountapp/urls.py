from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import accountapp.views

app_name = 'accountapp'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', accountapp.views.AccountCreateView.as_view(), name='create'), # Class Base View를 적을 때 as_view()로
    path('detail/<int:pk>', accountapp.views.AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', accountapp.views.AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', accountapp.views.AccountDeleteView.as_view(), name='delete'),
]
