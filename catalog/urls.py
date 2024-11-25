from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='author'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.BooksByUserListView.as_view(), name='my-borrowed'),
    path('allbooks/', views.AllborrowedBookList.as_view(), name='all-borrowed'),
    path('book/<int:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # Добавляем путь для выхода из системы
]