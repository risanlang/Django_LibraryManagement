from django.urls import path
from books import views 
 
urlpatterns = [ 
    path('books/', views.RuleOverview,name='Rule_Overview'),
    path('books/create/',views.add_book,name='Add_Book'),
    path('books/all/', views.book_list,name='BooksList'),
    path('books/delete/<int:pk>/',views.delete_book,name='Delete_Book'),
    path('books/update/<int:pk>/', views.update_book,name='Update_Book'),
]