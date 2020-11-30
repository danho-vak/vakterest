from django.urls import path
import accountapp.views
app_name = 'accountapp'

urlpatterns = [
    path('test/', accountapp.views.test, name='test')
]
