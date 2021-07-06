from django.shortcuts import render, redirect
from .models import Contact
from .filters import ContactFilter
# Create your views here.
def index(request):
    if request.method=='POST':
        contact = Contact()
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        language = request.POST.get('language')
        genre = request.POST.get('genre')
        contact.bookname=bookname
        contact.author=author
        contact.language=language
        contact.genre=genre
        contact.save()
        return redirect('details')
    return render(request,'index.html')
def details(request):
    contact = Contact.objects.all()
    # orders = contact.order_set.all()
    
    myFilter = ContactFilter(request.GET, queryset=contact)
    contact = myFilter.qs
    return render(request,'details.html',{'contact':contact,'myFilter':myFilter})