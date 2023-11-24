from django.urls import path
from . import views

urlpatterns = [
    path('suma/<int:num1>/<int:num2>/', views.suma, name='suma'),
    path('resta/<int:num1>/<int:num2>/', views.resta, name='resta'),
    path('multiplicacion/<int:num1>/<int:num2>/', views.multiplicacion, name='multiplicacion'),
    path('division/<int:num1>/<int:num2>/', views.division, name='division'),
]
