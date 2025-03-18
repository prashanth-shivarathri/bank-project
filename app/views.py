from django.shortcuts import render,redirect,HttpResponse
from . forms import Bankform
from . models import Bank
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate 
# Create your views here.
def home(request):
     return render(request,'home.html')

def index(request):
     form=Bankform()
     # print(form)
     if request.method=='POST':
          form=Bankform(request.POST,request.FILES)
          if form.is_valid():
               email=request.POST.get("email")
               form.save()
               # print(email)
               received_mail = email
               
               try:
                     send_mail(
                         "thanks for registration",# subject
                         f" USER REGISTER IN PRASHANTH DATA BASE ! \n thank you for registring we are excited to have you on board ! ,\n thank you \n regrads ", # body
                         settings.EMAIL_HOST_USER,
                         [received_mail],
                         fail_silently=False

                         )
                     print("mail sent ")
               except Exception as e:
                     return HttpResponse(f"Error sending email: {e}")
          return redirect('data')
     return render(request,'index.html',{'form':form}) 

def data(request):
     balance=0
     # data2=Bank.objects.get()
     if request.method=="POST":
          acc = request.POST.get("account")
          pin = int(request.POST.get('pin'))
          print(acc,pin)
          try:
               account=Bank.objects.get(account = acc)
               print(account.pin)
               print(account.email)
               email=account.email
          except:
               print("account not found")
          if account is not None:
               
               account.pin = pin
               # email=request.POST.get("email")
               account.save()
               received_mail = email
               
               try:
                     send_mail(
                         "thanks for registration",# subject
                         f" USER GENERATED OTP IN PRASHANTH DATA BASE ! \n thank you for registring we are excited to have you on board ! ,\n thank you \n regrads ", # body
                         settings.EMAIL_HOST_USER,
                         [received_mail],
                         fail_silently=False

                         )
                     print("mail sent ")
               except Exception as e:
                     return HttpResponse(f"Error sending email: {e}")
               
     
          return redirect("home")
     return render(request,'data.html',{'bal':balance})

def edit(request):
     data2=Bank.objects.get()
     if request.method=="POST":
        account=request.POST.get('account')
        pin=request.POST.get('pin')
        print(account,pin)
        data2.account=account
        data2.pin=pin
        data2.save()
        # print("updated successfully")
        return redirect("home") 
      
     return render(request,"edit.html",{'data':data2})



def balance(request):
     balance = 0
     if request.method=="POST":
          acc = request.POST.get("account")
          pin= request.POST.get("pin")
          print(acc,pin)
          try:

               account=Bank.objects.get(account = acc)
               print(account.name)
               print(account.email)
               
          except:
               print("account not found")
       
          if account.pin == int(pin):
               balance = account.balance
               
          else:
               print("invalid pin")
               return redirect("home")
     return render(request,'balance.html',{'bal':balance})


def add(request):
     acc=0
     bal=0
     
     if request.method=="POST":
          acc = request.POST.get("account")
          pin= request.POST.get("pin")
          bala=request.POST.get("balance")
          data2=Bank.objects.get(account=acc)
          data2=Bank.objects.get(pin=pin)

          print(acc,pin,bala)
          data2.account=acc
          data2.pin=int(pin)
          data2.balance+=int(bala)
          email=data2.email

          data2.save()
          
          received_mail = email
          print(email)
          try:
                     send_mail(
                         "thanks for registration",# subject
                         f" USER AMOUNT IS ADD TO UR ACCOUNT {data2.balance} ! \n thank you for registring we are excited to have you on board ! ,\n thank you \n regrads ", # body
                         settings.EMAIL_HOST_USER,
                         [received_mail],
                         fail_silently=False

                         )
                     print("mail sent ")

          except Exception as e:
                     return HttpResponse(f"Error sending email: {e}")

          try:

               account=Bank.objects.get(account = acc)
               # print(account.name)
               
               # print(email)
               
          except:
               print("account not found")
          
               
       
          if account.pin == int(pin):
              bal=account.balance
          else:
               print("invalid pin")
               
               
               



               

          # return redirect("home")
     return render(request,'add.html',{'bal':bal})


def withdraw(request):
     acc=0
     bal=0
     
     if request.method=="POST":
          acc = request.POST.get("account")
          pin= request.POST.get("pin")
          bala=request.POST.get("balance")
          data2=Bank.objects.get(account=acc)
          data2=Bank.objects.get(pin=pin)

          print(acc,pin,bala)
          data2.account=acc
          data2.pin=int(pin)
          data2.balance-=int(bala)
          email=data2.email
          data2.save()
          received_mail = email
          print(data2)
          try:
                     send_mail(
                         "thanks for registration",# subject
                         f" USER AMOUNT IS AMOUNT IS WITHDRAW TO UR ACCOUNT {data2.balance} ! \n thank you for registring we are excited to have you on board ! ,\n thank you \n regrads ", # body
                         settings.EMAIL_HOST_USER,
                         [received_mail],
                         fail_silently=False

                         )
                     print("mail sent ")

          except Exception as e:
                     return HttpResponse(f"Error sending email: {e}")

          try:

               account=Bank.objects.get(account = acc)
               print(account.name)
               
          except:
               print("account not found")
       
          if account.pin == int(pin):
              bal=account.balance
          else:
               print("invalid pin")
               return redirect("home")
     return render(request,'withdraw.html',{'bal':bal})


def transfer_bal(request):
     bal=0
     bal1=0
     if request.method == "POST":
          acc_from  = request.POST.get('account')
          acc_to  = request.POST.get('account1')
          pin  = request.POST.get('pin')
          amt  = request.POST.get('amt')
          # print(acc_from,acc_to,pin)
          

          try:
               account = Bank.objects.get(account=acc_from)
               account1 = Bank.objects.get(account=acc_to)
               print(account.name)
               
          except:
               print("account not found")
          if account.pin == int(pin):
               if account.balance > Decimal(amt):
                    account.balance -= Decimal(amt)
                    account1.balance += Decimal(amt)

                    account.save()
                    account1.save()
                    print(account.balance)
                    print(account1.balance)
                   
               else:
                    print("amt is insuffeient")
          else:
               print("enter the valid pin")
               return redirect("home")

     return render(request,'transfer_bal.html',{'acc':bal,'acc1':bal1})
