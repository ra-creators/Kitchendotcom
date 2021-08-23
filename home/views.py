from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import c_details, calculation

# Create your views here.
def kitchen_price_steps(request):
    return render(request, 'kitchen_price_steps.html')

def select_layout(request):
    return render(request, 'select_layout.html')

def customer_details(request):
    # store the choise and details of customer here
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        c_detail = c_details(name=name, email=email, phone=phone)  
        c_detail.save()

    return render(request, 'customer_details.html')

def l_shape(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        cal1 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch)
        cal1.save()
    return render(request, 'select_lshape.html')
def parallel(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        cal2 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch)
        cal2.save()
def straight(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        cal3 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch)
        cal3.save()
    
def ushape(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        c_feet = request.POST.get('c_feet')
        c_inch = request.POST.get('c_inch')
        cal1 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch, c_feet = c_feet, c_inch = c_inch)
        cal1.save()

def select_package(request):  # fqname is not confirmed
    if request.method == "POST":    
        final_cal = calculation()
        a = int(final_cal.a_feet) + (float(final_cal.a_inch) / 12)
        b = int(final_cal.b_feet) + (float(final_cal.b_inch) / 12)
        # if condition will be here for case of Ushape selection by user
        c = int(final_cal.c_feet) + (float(final_cal.c_inch) / 12)
        essentials = (a+b) * 5 * 1500
        premium = (a+b) * 5 * 1500
        deluxe = (a+b) * 5 * 2500
     
    return render(request, 'select_package.html', essentials, premium, deluxe) # 1.what for custom? 2.template name is not confirmed
