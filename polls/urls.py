from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:linguagem_id>/',views.detalhe,name='detalhe'),
    path('<int:linguagem_id>/quiz/',views.quiz,name='quiz'),
    path('<int:linguagem_id>/resultado/', views.resultado, name='resultado'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    
]