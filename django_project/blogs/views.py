from django.shortcuts import render
from .models import po_st

def index(request):
    context={
        'posts':po_st.objects.all()
    }
    return render(request,'blogs/home.html',context)

def about(request):
    return render(request,'blogs/about.html',{'title':'About'})
