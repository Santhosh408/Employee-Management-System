from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authapp.models import Addingemployee,Contactus


# Create your views here.
def Home(request):
    return render(request,"home.html")

def Signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')
        if password != confirm_password:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Username is Taken")
                return redirect('/signup')
        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect("/signup")
        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"User is created Please Login")
        return redirect('/login')
    return render(request,"signup.html")
    


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1= request.POST.get('pass1')
        myuser = authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")  
            return redirect('/login')  
    return render(request,"login.html")

def Logout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect("/login")

def Allemployees(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    username = request.user
    emp = Addingemployee.objects.filter(admin=username)
    return render(request,"emp/allemployees.html",{"allemployees":emp})

# def profile(request):
#     if not request.user.is_authenticated:
#         messages.warning(request,"Please Login and Try Again")
#         return redirect('/login')
#     user_phone = request.user
#     posts = Enrollment.objects.filter(Phonenumber=user_phone)
#     attendance = Attendance.objects.filter(phonenumber=user_phone)
#     context = {"posts":posts, "attendance":attendance}
#     return render(request,"profile.html",context)

def Contact(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    if request.method == "POST":
        # users = request.user.username
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        desc = request.POST.get('message')
        myquery = Contactus(name=name,email=email,subject=subject,description=desc)
        myquery.save()
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
    return render(request,'contact.html')


def Singleemployee(request):
    return render(request,"emp/allemployee.html")

def Addemployee(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    if request.method == "POST":
        usernamee = request.user 
        empid = request.POST.get('empid')
        empname = request.POST.get('empname')
        empemail = request.POST.get('empemail')
        empphone = request.POST.get('empphone')
        emprole = request.POST.get('emprole')
        empsalary = request.POST.get('empsalary')
        empaddress = request.POST.get('empaddress')
        myquery = Addingemployee(admin=usernamee,employeeid=empid,employeename=empname,employeeemail=empemail,employeephonenumber=empphone,employeerole=emprole,employeesalary=empsalary,employeeaddress=empaddress)
        myquery.save()
        messages.info(request,"Employee added Successfully")
        return redirect('/addemployee')
    return render(request,"emp/addemployee.html")


def employeedetails(request):
    pass

def deleteemployee(request,empid):
    e = Addingemployee.objects.get(pk = empid)
    e.delete()
    messages.info(request,"Deleted Successfully!")
    return redirect("/allemployees")

def updateemployee(request,empid):
    emp = Addingemployee.objects.get(pk = empid)
    return render(request,"emp/updateemployee.html",{"employee":emp})

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"service.html")

def doupdateemployee(request,empid):
    if request.method == "POST":
        emp = Addingemployee.objects.get(pk=empid)
        # usernamee = request.user 
        emp.employeeid = request.POST.get('empid')
        emp.employeename = request.POST.get('empname')
        emp.employeeemail = request.POST.get('empemail')
        emp.employeephonenumber = request.POST.get('empphone')
        emp.employeerole = request.POST.get('emprole')
        emp.employeesalary = request.POST.get('empsalary')
        emp.employeeaddress = request.POST.get('empaddress')
        emp.save()
        messages.info(request,"Employee details updated added Successfully")
        return redirect('/allemployees')
