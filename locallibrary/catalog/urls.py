from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('boks/', views.BokListView.as_view(), name='boks'),
    path('bok/<int:pk>', views.BokDetailView.as_view(), name='book-detail'),
    path('bks/', views.BkListView.as_view(), name='bks'),
    path('bk/<int:pk>', views.BkDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:id>', views.AuthorDetailView.as_view(), name='author-detail'),
    ]
