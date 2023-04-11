from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
   context={'name':'harry','course':'Django'}
   return render(request, 'home.html',context)

def about(request):
   #return HttpResponse("This is About")
   return render(request, 'about.html')

def projects(request):
   return render(request,'projects.html')

def contact(request):
   if request.method == 'POST':
      #print("This is post")
      name=request.POST['name']
      mail=request.POST['mail']
      phone=request.POST['phone']
      desc=request.POST['desc']
      print(name, mail, phone)
      ins=Contact(name=name, mail=mail, phone=phone,desc=desc)
      ins.save()
      print("the data has been written to the database")
      
   return render(request,'contact.html')

def experience(request):
   return render(request,'experience.html')

def footer(request):
   return render(request,'footer.html')