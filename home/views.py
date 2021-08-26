from django.http.response import HttpResponse
from django.http import HttpResponseRedirect  
from django.shortcuts import redirect, render  
from home.models import c_details, calculation, kitchen_details

# Create your views here.
def kitchen_price_steps(request):
    return render(request, 'kitchen_price_steps.html')

def select_layout(request):
    if request.method == "POST":
        layout = request.POST.get('kitchenLayout')
        select_layout = kitchen_details(layout = layout)
        select_layout.save()
        return redirect('/customer_details')    
    return render(request, 'select_layout.html')

def customer_details(request):
    #selected_layout = kitchen_details()
    #final_layout = selected_layout.layout
    # store the choise and details of customer here
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        c_detail = c_details(name=name, email=email, phone=phone)  
        c_detail.save()
    return render(request, 'customer_details.html')

# logic required for rendering selected layout's page

def l_shape(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        cal1 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch, c_feet = 0, c_inch = 0)
        cal1.save()
    return render(request, 'select_lshape.html')

def parallel(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        # b_feet = request.POST.get('b_feet')
        # b_inch = request.POST.get('b_inch')
        cal2 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = a_feet, b_inch = a_inch, c_feet = 0, c_inch = 0)
        cal2.save()
    return render(request, 'select_parallel.html')

def straight(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        cal3 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch, c_feet = 0, c_inch = 0)
        cal3.save()
    return render(request, 'select_straight.html')

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
    return render(request, 'select_ushape.html')

def select_package(request):  # fqname is not confirmed
    
    final_cal = calculation()
    a = int(final_cal.a_feet) + (float(final_cal.a_inch) / 12)
    b = int(final_cal.b_feet) + (float(final_cal.b_inch) / 12)
    l = int(final_cal.loft)
    # if condition will be here for case of Ushape selection by user
    c = int(final_cal.c_feet) + (float(final_cal.c_inch) / 12)
    # c will be ZERO for cases apart from Ushape
    essentials = (a+b+c) * (3+l) * 1800
    premium = (a+b+c) * (3+l) * 2100
    deluxe = (a+b+c) * (3+l) * 2500
    if request.method == "POST":    
        package = request.POST.get('package') # "package" <- this name might be different
    # custom calculation remaining

    return render(request, 'select_package.html', essentials, premium, deluxe) # 1.what for custom? 2.template name is not confirmed

def select_loft_type(request):
    if request.method == "POST":
        loft1 = request.POST.get('loft') # this keyword depends on template
        cal5 = calculation(loft = loft1)
        cal5.save()
    return render(request, "select_loft_type.html")

def select_loft(request):
    if request.method == "POST":
        ans = request.POST.get('loft')
        loft = kitchen_details(loft = ans)
        loft.save()
    return render(request, "select_loft_type")

def select_countertop(request):
    if request.method == "POST":
        c_top = request.POST.get('countertop')
        countertop = kitchen_details(Countertop = c_top)
        countertop.save()
    return render(request, 'select_countertop.html')

def select_finish(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        finish = kitchen_details(Finish = f)
        finish.save()
    return render(request, 'select_finish.html')

def select_accessories(request):
    if request.method == "POST":
        acc = request.POST.get('accessories')
        accessories = kitchen_details(Accessories = acc)
        accessories.save()
    return render(request, 'select_accessories.html')

def select_appliances(request):
    if request.method == "POST":
        app_list = []
        # work inprogress
    return render(request, 'select_appliances.html')