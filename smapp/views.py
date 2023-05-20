from django.contrib.auth import authenticate,login,logout
from urllib import request
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import allowed_users, unautheticated_user
from django.contrib.sessions.models import Session 
from datetime import datetime
from django.core.paginator import Paginator

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        email= request.POST.get('email')
        username=request.POST.get('username')
        fullname=request.POST.get('fullname')
        gender=request.POST.get('gender')
        mobile_no=request.POST.get('mobileno')
        photo=request.POST.get('photo')
        role=request.POST.get('role')
        password=request.POST.get('password')
        userobj=User.objects.create_user(email=email,username=username,fullname=fullname,gender=gender,mobile_no=mobile_no,photo=photo,role=role,password=password)
        userobj.save()

    return render(request,'register.html')

def AddProduct(request):
    if request.method=="POST" :
        name= request.POST.get('name')
        sku=request.POST.get('sku')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        photo=request.FILES['image']
        prod=product(prod_name=name,prod_sku=sku,prod_price=price,prod_quantity=quantity,prod_image=photo)
        prod.save()
    
    return render(request,'addProductForm.html')

@login_required(login_url='LogIn')
def ShowProduct(request):
    if request.user.role != 'supplier':
        return HttpResponse("You are not Authorized")
    else:
        prod=product.objects.all()
        context={"form":prod}
        return render(request,'ProductTable.html',context=context)

@unautheticated_user
def view_login(request):
    try:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                user=request.user
                if user.role == 'supplier':
                    return redirect("supplierpage")
                elif user.role == 'retailer':
                    return redirect("retailerpage")
            else:
                messages.error(request, 'invalid login credentials')
                return redirect("LogIn")  
        else:
            return render(request,"LogIn.html")
    except Exception as e:
        print(e)

def logout_view(request):
    logout(request)
    return redirect('LogIn')

def delete_row(request,id):
    prod=product.objects.get(id=id)
    prod.delete()
    return redirect("productTable")

def show_product_row(request,id):
    prod=product.objects.get(id=id)
    context={"data":prod}
    return render(request,'showProductRow.html',context=context)

def edit_product_row(request,id):
    try:
        prod=product.objects.get(id=id)
        if request.method=='POST':
            prod.prod_name= request.POST.get('name')
            prod.prod_sku=request.POST.get('sku')
            prod.prod_price=request.POST.get('price')
            prod.prod_quantity=request.POST.get('quantity')
            prod.prod_image=request.FILES['image']
            prod.save()
            return redirect("productTable")
    except Exception as e:
        print(e)

@login_required(login_url='LogIn')
def retailer_table(request):
    if request.user.role != 'retailer':
        return HttpResponse("You are not Authorized")
    else:
        prod=product.objects.all()
        pageNo=request.GET.get('pageNo',1)
        print(pageNo)
        pageSize=2
        totPage=len(prod)/int(pageSize)
        if int(pageNo)==1:
            prevPage=1
        else:
            prevPage=int(pageNo)-1
        if int(pageNo)==int(totPage):
            nextPage=int(totPage)
        else:
            nextPage=int(pageNo)+1
        paginator = Paginator(prod, pageSize)
        products=paginator.get_page(pageNo)
        
        pageList=[]
        for i in range(1,int(totPage)+1):
            pageList.append(i)        
        context={"form":products,"totpage":pageList,"prevpage":prevPage,"nextpage":nextPage}
        return render(request,'retailerTable.html',context=context)

def buy_product(request,id):
    prod=product.objects.get(id=id)
    if request.method=="POST" :
        prod.items_bought = request.POST.get('selectedQuantity')
        prod.prod_quantity = (int)(prod.prod_quantity) - (int)(prod.items_bought)
        prod.save()
        rname=request.user
        psku=prod.prod_sku
        pname=prod.prod_name
        pquant=prod.items_bought
        date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        retailerinfo=retailerData(ret_name=rname,p_sku=psku,p_name=pname,p_quantity=pquant,date=date)
        retailerinfo.save()
    return redirect("retailerTable")

@login_required(login_url='LogIn')
def supplier_page(request):
    if request.user.role != 'supplier':
        return HttpResponse("You are not Authorized")
    else:
        return render(request,'supplierpage.html')

@login_required(login_url='LogIn')
def purchase_history(request):
    rd=retailerData.objects.all()
    context={"form":rd}
    return render(request,'purchaseHistory.html',context=context)

@login_required(login_url='LogIn')
def retailer_page(request):
    if request.user.role != 'retailer':
        return HttpResponse("You are not Authorized")
    else:
        return render(request,'retailerpage.html')

@login_required(login_url='LogIn')
def retailer_history(request):
    user=request.user
    rd=retailerData.objects.filter(ret_name=user).values('p_sku','p_name','p_quantity','date').distinct()
    context={"form":rd}
    return render(request,'retailerHistory.html',context=context)