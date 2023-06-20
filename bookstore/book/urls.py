from django.urls import path
from .import views
from .views import BookList, BookDetail, BookCheckoutView, PaymentComplete, SearchResultsView

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',SearchResultsView.as_view(),name='search-results'),
    path('booklist/',BookList.as_view(),name='books'),
    path('bookdetails/<int:pk>/',BookDetail.as_view(),name='details'),
    path('checkout/<int:pk>/',BookCheckoutView.as_view(),name='checkout'),
    path('complete/',PaymentComplete,name='complete')
]