from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('books/<int:book_id>', views.book_view),
    path('addbook', views.add_book),
    path('addpublisher', views.add_publisher),
    path('addrelationship', views.add_relationship),
]