from django.shortcuts import get_object_or_404, render

# Create your views here.
# https://www.kaggle.com/datasets/saurabhbagchi/books-dataset

from .models import Books
from .forms import BookSearchForm

def search_books(request):
    if request.method == 'GET':
        form = BookSearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            # Perform a case-insensitive search on title and author fields
            books = Books.objects.filter(title__icontains=search_query) | \
                    Books.objects.filter(author__icontains=search_query)
            return render(request, 'books/index.html', {'books': books, 'form': form})
    else:
        form = BookSearchForm()
    return render(request, 'books/index.html', {'form': form})

def book_detail(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})