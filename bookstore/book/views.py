from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, order


# Create your views here.
def home(request):
    return render(request,'home.html')

class SearchResultsView(ListView):
     model=Book
     template_name='search_results.html'

     def get_queryset(self):
        query=self.request.GET.get('q')
        return Book.objects.filter(
             Q(title=query) | Q(author=query)
         )


class BookList(ListView):
    model=Book
    context_object_name = 'books'
    template_name = 'booklist.html'

class BookDetail(DetailView):
    model=Book
    context_object_name = 'books'
    template_name = 'bookdetail.html'

class BookCheckoutView(DetailView):
    model=Book
    template_name = 'checkout.html'

def PaymentComplete(request,pk):
    product=Book.objects.get(id=pk)
    order.objects.create(
        product=product
    )
    return JsonResponse('Payment Completed',safe=False)




