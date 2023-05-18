from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,FormView,View,UpdateView,ListView
from django.contrib.auth.models import User
from olxweb.forms import Registrationform,LoginForm,UserprofileForm,ProductForm
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate,logout
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from api.models import Userprofile,Products,carts,Questions,Answers,Soldoutproducts
# Create your views here.
def sigin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
decs=[sigin_required,never_cache]

class Signupview(CreateView):
    form_class=Registrationform
    model=User
    template_name="register.html"
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request, "Account created successfully")
        return super().form_valid(form)
class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"account created seccessfully")
                return redirect("home")
            else:
                messages.error(request,"provided credentials are invalid")
                return render(request,"login.html",{"form":form})

@method_decorator(decs,name='dispatch')
class Indexview(CreateView,ListView):
    model=Products
    form_class=ProductForm
    template_name="index.html"
    success_url=reverse_lazy("home")
    context_object_name="products"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class Userprofilecreateview(CreateView):
    model=Userprofile
    form_class=UserprofileForm
    template_name="profile-add.html"
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
class Profiledetailview(View):
    def get(self,request,*args,**kwargs):
        qs=Userprofile.objects.filter(user=request.user,is_active=True)
        return render(request,"profile-details.html",{"profile":qs})

class Profileupdateview(UpdateView):
    model=Userprofile
    template_name="profileupdate.html"
    form_class=UserprofileForm
    success_url=reverse_lazy("home")
    pk_url_kwarg="id"

class productAddView(CreateView):
    model=Products
    form_class=ProductForm
    template_name="product-add.html"
    success_url=reverse_lazy("home")

class ProductDetailView(View):
    def get(self,request,*args,**kwargs):
            id=kwargs.get("id")
            qs=Products.objects.get(id=id)
            return render(request,"product-detail.html",{"product":qs})

class AddtocartView(View):
    def post(self,request,*args,**kwargs):
        qty=request.POST.get("qty")
        user=request.user
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        carts.objects.create(product=product,user=user,qty=qty)
        return redirect("home")

class CartListView(View):
    def get(self,request,*args,**kwargs):
        qs=carts.objects.filter(user=request.user,status="product added").order_by("-id")
        return render(request,"saved-list.html",{"carts":qs})
    
class CartRemoveview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        carts.objects.filter(id=id).update(status="cancelled")
        return redirect("home")
    
class AddquestionView(View):
    def post(self,request,*args,**kwargs):
        qid=kwargs.get("id")
        ques=Questions.objects.get(id=qid)
        usr=request.user
        ans=request.POST.get("question")
        Questions.objects.create(user=usr,questions=ques,answer=ans)
        return redirect("home")
    
class AddanswerView(View):
    def post(self,request,*args,**kwargs):
        qid=kwargs.get("id")
        ques=Answers.objects.get(id=qid)
        usr=request.user
        ans=request.POST.get("answer")
        Answers.objects.create(user=usr,questions=ques,answer=ans)
        return redirect("home")
    
class OrderView(View):
    def get(self,request,*args,**kwargs):
        qs=Soldoutproducts.objects.filter(user=request.user)
        return render(request,"order-list.html",{"order":qs})


class Signoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")