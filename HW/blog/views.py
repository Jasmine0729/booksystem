#coding=utf8
#from django.shortcuts import render
#import MySQLdb
#from django.template import Context
from django.shortcuts import render_to_response
#from django.http import HttpResponse
from models import Author
from models import Book
# Create your views here.

def add_book(request):
    if 'PublishDate' in request.POST and request.POST:
        post = request.POST
        ID = int(post['AuthorID'])
        author = Author.objects.get(AuthorID = ID)
        new_book = Book(
           ISBN=post['ISBN'],
           Title=post['Title'],
           #AuthorID=author,
           Publisher=post['Publisher'],
           PublishDate=post['PublishDate'],
           Price=post['Price'],
           )
        new_book.save()
        book_list = Book.objects.all()
        return render_to_response("AllInformation.html",{"book_list":book_list})
    save_book = Book.objects.all()
    return render_to_response("AddBook.html",{"save_book":save_book})

def add_author(request):
    if 'AuthorID' in request.POST and request.POST:
        post = request.POST
        new_author = Author(
            AuthorID = int(post['AuthorID']),
            Name = post['Name'],
            Age = post['Age'],
            Country = post['Country'],
        )
        new_author.save()
        book_list = Book.objects.all()
        return render_to_response("AllInformation.html",{"book_list":book_list})
    save_author = Author.objects.all()
    return render_to_response("AddAuthor.html",{"save_author":save_author})

def all_information(request):
    if request.POST:
        post = request.POST
        search_author = post['search']
        temp_author = Author.objects.get(Name = search_author)
        if temp_author:
            temp_books = Book.objects.filter(AuthorID = temp_author).all()
            return render_to_response("Search.html",{"temp_books":temp_books})
    book_list = Book.objects.all()
    return render_to_response("AllInformation.html",{"book_list":book_list})

def delete_information(request):
    book_id = request.GET["id"]
    d = Book.objects.filter(ISBN = book_id)
    d.delete()
    book_list = Book.objects.all()
    return render_to_response("AllInformation.html",{"book_list":book_list})
    
def show_detail(request):
    #if 'idtwo' in request.GET and request.GET:
        b_id = request.GET['idtwo']
        detail_book = Book.objects.get(ISBN = b_id)
        detail_author = detail_book.AuthorID
        return render_to_response("Detail.html",{"detail_book":detail_book,"detail_author":detail_author})
    #else:
     #   book_list = Book.objects.all()
      #  return render_to_response("AllInformation.html",{"book_list":book_list})

#def search(request):
    #if request.POST and "search" in request.POST:
 #   if request.POST:
  #      post = request.POST
  #      search_author = post['search']
  #      temp_author = Author.objects.get(Name = search_author)
  #      if temp_author:
  #          temp_books = Book.objects.filter(AuthorID = temp_author).all()
  #          return render_to_response("Search.html",{"temp_books":temp_books})
    #else:
     #   book_list = Book.objects.all()
      #  return render_to_response("AllInformation.html",{"book_list":book_list})