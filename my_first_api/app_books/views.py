from django.shortcuts import render
from .models import Books
from rest_framework.views import APIView
from rest_framework.views import Response
from django.forms import model_to_dict

# Create your views here.

class BooksView(APIView):
    def get(self, request):
        books = Books.objects.all().values()
        return Response({'book': list(books)})
    
    def post(self, request):
        new_book = Books.objects.create(
            book_name_uz = request.data['book_name_uz'],
            book_name_en = request.data['book_name_en'],
            about_uz = request.data['about_uz'],
            about_en = request.data['about_en'],
        )
        return Response({'new_book': model_to_dict(new_book)})
    

    def delete(self, request):
            try:
                 books_id = request.data['books_id']
                 Books.objects.filter(pk = books_id).delete()
                 return Response({'reslut': 'success', 'desc': f'Book with id{books_id} succesfully'})
            except:
                 return Response({'result': 'error', 'desc': 'Internal server error! Please, try again later'})
            