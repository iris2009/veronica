# -*- coding: cp936 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app.models import Book, Author
from django.template import Context, RequestContext
from django.http import HttpResponseRedirect
# Create your views here.
#encoding=utf-8
# -*- coding: cp936 -*-
def library(request):
    bookset = []
    bookinformation = []
    authorinformation = []
    ALLset = Book.objects.all()
    if request.GET:
        post = request.GET
        
        if post.has_key('insertorupdate'):#insert or update
            new_book = Book(
                ISBN = post["ISBN"],
                Title=post['Title'],
                AuthorID = post["AuthorID"],
                Publisher = post["Publisher"],
                PublishDate = post["PublishDate"],
                Price = post['Price'])
            dset = Book.objects.filter(ISBN = post['ISBN']) 
            if len(dset) != 0: #delete the repetitive book
                dset[0].delete()
            new_book.save()
            dset = Author.objects.filter(AuthorID = post['AuthorID'])
            if len(dset) == 0:  # add an author
                new_author = Author(
                    AuthorID = post['AuthorID'],
                    Name = post['AuthorName'],
                    Age = post['AuthorAge'],
                    Country = post['AuthorCountry'])
                new_author.save()
                
        if post.has_key('delete'): #delete the book
            dset = Book.objects.filter(ISBN = post['ISBN'])
            if len(dset) != 0:
                aset = Book.objects.filter(AuthorID = dset[0].AuthorID)
                if len(aset) == 1:
                    bset = Author.objects.filter(AuthorID = dset[0].AuthorID)
                    bset[0].delete()  #delete the author
                dset[0].delete()
                
        for i in ALLset:
            if post.has_key(i.Title):#show information of a book
                oneq = []
                oneq.append(i)
                bookinformation = [] + oneq
                authorinformation = Author.objects.filter(AuthorID = i.AuthorID)
                break
            if post.has_key(i.ISBN): #delete the book
                aset = Book.objects.filter(AuthorID = i.AuthorID)
                if len(aset) == 1:
                    bset = Author.objects.filter(AuthorID = i.AuthorID)
                    bset[0].delete()  #delete the author
                i.delete()
                break

        if post.has_key('toselect'):#search
            authorset = Author.objects.filter(Name = post['authorselect'])
            if len(authorset) != 0:
                bookset = Book.objects.filter(AuthorID = authorset[0].AuthorID)
                
    ALLset = Book.objects.all()
    
    
    return render_to_response('Book.html', {'ALLset': ALLset, 'ONE': bookinformation, \
    'AUTHOR': authorinformation, 'Bookset': bookset}, context_instance=RequestContext(request))
def xxx(request):
    dset = []
    cset = []
    ID = ""
    if request.GET:
        ID  = request.GET["aTitle"]
        dset = Book.objects.filter(Title = ID)
        a = dset[0].AuthorID
        cset = Author.objects.filter(AuthorID = a)
    return render_to_response("xxx.html",{"ONE":dset, "AUTHOR":cset,'id':ID}, context_instance=RequestContext(request))
    

