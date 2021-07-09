from django.shortcuts import render, redirect
from .models import Contact
from .filters import ContactFilter
from django.views.generic import ListView
from taggit.models import Tag
# Create your views here.
class TagMixin(object):
    def get_context_data(self,**kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags']=Tag.objects.all()
        return context
def index(request):
    if request.method=='POST':
        contact = Contact()
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        language = request.POST.get('language')
        genre = request.POST.get('genre')
        booktags = request.POST.get('booktags')
        contact.bookname=bookname
        contact.author=author
        contact.language=language
        contact.genre=genre
        contact.save()
        for tag in booktags:
                contact.tags.add(tag)
        return redirect('details')
    return render(request,'index.html')
    
def details(request):
    contact = Contact.objects.all()    
    myFilter = ContactFilter(request.GET, queryset=contact)
    contact = myFilter.qs
    return render(request,'details.html',{'contact':contact,'myFilter':myFilter})

class TagIndexView(TagMixin,ListView):
    model = Contact
    template_name = 'tags.html'
    context_object_name = 'contact'
    def get_queryset(self):
        return Contact.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
