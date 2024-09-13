from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import ToDo
from ToDo.forms import ToDoForm
# Create your views here.

class MainView(LoginRequiredMixin,View):
    def get(self,request):
        r=ToDo.objects.all()
        ctx={'ToDo_list':r}
        return render(request,'ToDo/ToDo_list.html',ctx)


class OpenView(View) :
    def get(self, request):
        return render(request, 'ToDo/logout_view.html')

class ToDoCreateView(View):
    def get(self,request):
        form=ToDoForm()
        ctx={"form":form}
        return render(request,"ToDo/ToDo_form.html",ctx)

    def post(self,request):
        form=ToDoForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,"ToDo/ToDo_form.html",ctx)

        ToDo=form.save()
        return render(request,"ToDo/ToDo_success.html")

#from django.shortcuts import render
#from .models import Post
# Create your views here.


#def ToDo_list(request):
 #   post = Post.objects.all()
 #   context = { 'ToDo_list':post }
 #   return render(request,'ToDo/ToDo_list.html',context)