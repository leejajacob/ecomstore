from django.urls import path
from .import views
from .views import BookList, BookDetail, BookCheckoutView, PaymentComplete, SearchResultsView, cart, add_to_cart, \
    remove_from_cart

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',SearchResultsView.as_view(),name='search-results'),
    path('booklist/',BookList.as_view(),name='books'),
    path('bookdetails/<int:pk>/',BookDetail.as_view(),name='details'),
    path('checkout/<int:pk>/',BookCheckoutView.as_view(),name='checkout'),
    path('complete/',PaymentComplete,name='complete'),
    path('cart/',cart,name='mycart'),
    path('cart/add/<int:book_id>/',add_to_cart,name='add_to_cart'),
    path('cart/remove/<int:book_id>/',remove_from_cart,name='remove_from_cart')
]