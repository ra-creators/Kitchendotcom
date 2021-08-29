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
    # store the choise and details of customer here
    context = kitchen_details.objects.all().last()
    # selected_layout = sizeof(context)
    
    # print(context)
    # print('Pratham')

    # print(type(selected_layout))
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        c_detail = c_details(name=name, email=email, phone=phone)  
        c_detail.save()
        if context.layout == "L":
            return redirect('/select_lshape')
        elif(context.layout == 'S'):
            return redirect('/select_straight')
        elif(context.layout == 'U'):
            return redirect('/select_ushape')
        elif(context.layout == 'P'):
            return redirect('/select_parallel')
    return render(request, 'customer_details.html')

# logic required for rendering selected layout's page

def lshape(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        cal1 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch, c_feet = 0, c_inch = 0)
        cal1.save()
        return redirect('/select_loft_type')
    return render(request, 'select_lshape.html')

def parallel(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        cal2 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch, c_feet = 0, c_inch = 0)
        cal2.save()
        return redirect('/select_loft_type')
    return render(request, 'select_parallel.html')

def straight(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        print(a_feet)
        cal3 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = 0, b_inch = 0, c_feet = 0, c_inch = 0)
        # print(cal3)
        cal3.save()
        return redirect('/select_loft_type')
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
        return redirect('/select_loft_type')
    return render(request, 'select_ushape.html')

# def select_loft(request):
#     if request.method == "POST":
#         ans = request.POST.get('loft')
#         loft = kitchen_details(loft = ans)
#         loft.save()
#     return render(request, "select_loft_type")

def select_loft_type(request):
    # final_cal = calculation.objects.all().last()
    
    if request.method == "POST":
        loft1 = request.POST.get('loft_type') # this keyword depends on template
        if loft1 == "custom":
            loft1 = request.POST.get('loft')
        select_layout = kitchen_details(loft = loft1)
        select_layout.save()
        return redirect('/select_package')
    return render(request, "select_loft_type.html")

def select_package(request):  # fqname is not confirmed
    
    final_cal = calculation.objects.all().last()
    s_loft = kitchen_details.objects.all().last()
    print(int(final_cal.a_feet))
    print(int(s_loft.loft))
    a = int(final_cal.a_feet) + (int(final_cal.a_inch) / 12)
    b = int(final_cal.b_feet) + (int(final_cal.b_inch) / 12)
    l = int(s_loft.loft)
    # if condition will be here for case of Ushape selection by user
    c = int(final_cal.c_feet) + (int(final_cal.c_inch) / 12)
    # custom calculation remaining

    context = {
    "essentials" : (a+b+c) * (3+l) * 1800,
    "premium" : (a+b+c) * (3+l) * 2100,
    "deluxe" : (a+b+c) * (3+l) * 2500
    }
    
    if request.method == "POST":    
        package = request.POST.get('package') # "package" <- this name might be different
        
        print(package)
    # custom calculation remaining

    return render(request, 'select_package.html',context) # 1.what for custom? 2.template name is not confirmed

def select_package_essentials(request):
    return render(request, 'select_package_essentials.html')

def select_package_luxe(request):
    return render(request, 'select_package_luxe.html')

def select_package_premium(request):
    return render(request, 'select_package_premium.html')

def select_package_buildpkg(request):
    return render(request, 'select_package_buildpkg.html')

def build_package(request):
    if request.method == "POST":    
        material = request.POST.get('ownpackage')
        print(material)
    return render(request, 'build_package.html')    

def build_package_hdhmr(request):
    return render(request, 'build_package_hdhmr.html')

def build_package_mrply(request):
    return render(request, 'build_package_mrply.html')

def build_package_bwrply(request):
    return render(request, 'build_package_bwrply.html')

def build_package_bwpply(request):
    return render(request, 'build_package_bwpply.html')


def select_countertop(request):
    if request.method == "POST":
        c_top = request.POST.get('countertop')
        countertop = kitchen_details(Countertop = c_top)
        countertop.save()
    return render(request, 'select_countertop.html')

def select_finish(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        print(f)
        finish = kitchen_details(Finish = f)
        finish.save()
    return render(request, 'select_finish.html')

def select_finish_laminate(request):
    return render(request, 'select_finish_laminate.html')

def select_finish_pvclaminate(request):
    return render(request, 'select_finish_pvclaminate.html')

def select_finish_asacrylic(request):
    return render(request, 'select_finish_asacrylic.html')

def select_finish_glossypu(request):
    return render(request, 'select_finish_glossypu.html')

def select_accessories(request):
    if request.method == "POST":
        acc = request.POST.get('accessories')
        print(acc)
        accessories = kitchen_details(Accessories = acc)
        accessories.save()
    return render(request, 'select_accessories.html')

def select_accessories_basic(request):
    return render(request, 'select_accessories_basic.html')

def select_accessories_intermediate(request):
    return render(request, 'select_accessories_intermediate.html')

def select_accessories_premium(request):
    return render(request, 'select_accessories_premium.html')

def select_services(request):
    if request.method == "POST":
        app_list = []
        # work inprogress
    return render(request, 'select_services.html')


def select_appliances(request):
    if request.method == "POST":
        app_list = []
        # work inprogress
    return render(request, 'select_appliances.html')
