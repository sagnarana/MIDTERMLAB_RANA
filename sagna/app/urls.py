from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
   path('home/', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('login/', views.login_page, name='login'),
    
    path('authors/', views.author_list, name='author_list'),
    path('publishers/', views.publisher_list, name='publisher_list'),  # Corrected URL pattern
    path('books/', views.book_list, name='book_list'),
    path('customers/', views.customer_list, name='customer_list'),
    path('orders/', views.order_list, name='order_list'),
    
    
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/new/', views.author_create, name='author_create'),
    path('authors/<int:pk>/edit/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
    
    ]   

   
    
