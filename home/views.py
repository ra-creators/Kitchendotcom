from django.http.response import HttpResponse
from django.http import HttpResponseRedirect  
from django.shortcuts import redirect, render  
from home.models import c_details, calculation, kitchen_details

# Create your views here.
def kitchen_price_steps(request):
    # request.session['name'] = 'test'
    return render(request, 'kitchen_price_steps.html')

def select_layout(request):
    # name = request.session.get('name')
    # print(name)
    if request.method == "POST":
        layout = request.POST.get('kitchenLayout')
        request.session['layout'] = layout 
        print(layout)
        select_layout = kitchen_details(layout = layout)
        select_layout.save()
        return redirect('/customer_details')
      
    return render(request, 'select_layout.html')

def customer_details(request):
    layout = request.session.get('layout')
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
        request.session['name'] = name
        c_detail = c_details(name=name, email=email, phone=phone)  
        c_detail.save()
        if layout == "L":
            return redirect('/select_lshape')
        elif(layout == 'S'):
            return redirect('/select_straight')
        elif(layout == 'U'):
            return redirect('/select_ushape')
        elif(layout == 'P'):
            return redirect('/select_parallel')
    return render(request, 'customer_details.html')

# logic required for rendering selected layout's page

def lshape(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        b_feet = request.POST.get('b_feet')
        b_inch = request.POST.get('b_inch')
        request.session['a_feet'] = a_feet
        request.session['a_inch'] = a_inch
        request.session['b_feet'] = b_feet
        request.session['b_inch'] = b_inch 
        request.session['c_feet'] = 0
        request.session['c_inch'] = 0
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
        request.session['a_feet'] = a_feet
        request.session['a_inch'] = a_inch
        request.session['b_feet'] = b_feet
        request.session['b_inch'] = b_inch 
        request.session['c_feet'] = 0
        request.session['c_inch'] = 0
        cal2 = calculation(a_feet = a_feet, a_inch = a_inch, b_feet = b_feet, b_inch = b_inch, c_feet = 0, c_inch = 0)
        cal2.save()
        return redirect('/select_loft_type')
    return render(request, 'select_parallel.html')

def straight(request):
    if request.method == "POST":
        a_feet = request.POST.get('a_feet')
        a_inch = request.POST.get('a_inch')
        request.session['a_feet'] = a_feet
        request.session['a_inch'] = a_inch
        request.session['b_feet'] = 0
        request.session['b_inch'] = 0
        request.session['c_feet'] = 0
        request.session['c_inch'] = 0
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
        request.session['a_feet'] = a_feet
        request.session['a_inch'] = a_inch
        request.session['b_feet'] = b_feet
        request.session['b_inch'] = b_inch
        request.session['c_feet'] = c_feet
        request.session['c_inch'] = c_inch
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
            request.session['loft'] = loft1 # for if condition
        request.session['loft'] = loft1     # for else condition
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
    
    # to be entered in followinf 4 function
    if request.method == "POST":    
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        print(package)
    # 
    # custom calculation remaining
        if package == "ownpackage":
            return redirect('/build_package')
        else:
            return redirect('/summary')

    return render(request, 'select_package.html',context) # 1.what for custom? 2.template name is not confirmed

def select_package_essentials(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        return redirect('/summary')
    
    return render(request, 'select_package_essentials.html')

def select_package_luxe(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        return redirect('/summary')
    return render(request, 'select_package_luxe.html')

def select_package_premium(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        return redirect('/summary')
    return render(request, 'select_package_premium.html')

def select_package_buildpkg(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        return redirect('/build_package')
    return render(request, 'select_package_buildpkg.html')

def build_package(request):
    if request.method == "POST":    
        material = request.POST.get('ownpackage')
        request.session['material'] = material
        return redirect('/select_countertop')
    return render(request, 'build_package.html')    

def build_package_hdhmr(request):
    if request.method == "POST": 
        material = request.POST.get('ownpackage')
        request.session['material'] = material
        return redirect('/select_countertop')

    return render(request, 'build_package_hdhmr.html')

def build_package_mrply(request):
    if request.method == "POST":  
        material = request.POST.get('ownpackage')
        request.session['material'] = material
        return redirect('/select_countertop')
    return render(request, 'build_package_mrply.html')

def build_package_bwrply(request):
    if request.method == "POST":  
        material = request.POST.get('ownpackage')
        request.session['material'] = material
        return redirect('/select_countertop')
    return render(request, 'build_package_bwrply.html')

def build_package_bwpply(request):
    if request.method == "POST":  
        material = request.POST.get('ownpackage')
        request.session['material'] = material
        return redirect('/select_countertop')
    return render(request, 'build_package_bwpply.html')


def select_countertop(request):
    if request.method == "POST":
        c_top = request.POST.get('countertop')
        request.session['countertop'] = c_top
        countertop = kitchen_details(Countertop = c_top)
        countertop.save()
        return redirect('/select_finish')
    return render(request, 'select_countertop.html')

def select_finish(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        request.session['finish'] = f
        print(f)
        finish = kitchen_details(Finish = f)
        finish.save()
        return redirect('/select_accessories')
    return render(request, 'select_finish.html')

def select_finish_laminate(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        request.session['finish'] = f
        return redirect('/select_accessories')
    return render(request, 'select_finish_laminate.html')

def select_finish_pvclaminate(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        request.session['finish'] = f
        return redirect('/select_accessories')
    return render(request, 'select_finish_pvclaminate.html')

def select_finish_asacrylic(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        request.session['finish'] = f
        return redirect('/select_accessories')
    return render(request, 'select_finish_asacrylic.html')

def select_finish_glossypu(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        request.session['finish'] = f
        return redirect('/select_accessories')
    return render(request, 'select_finish_glossypu.html')

def select_accessories(request):
    if request.method == "POST":
        acc = request.POST.get('accessories')
        request.session['accessories'] = acc
        print(acc)
        accessories = kitchen_details(Accessories = acc)
        accessories.save()
        return redirect('/select_services')
    return render(request, 'select_accessories.html')

def select_accessories_basic(request):
    if request.method == "POST":
        acc = request.POST.get('accessories')
        request.session['accessories'] = acc
        return redirect('/select_services')
    return render(request, 'select_accessories_basic.html')

def select_accessories_intermediate(request):
    if request.method == "POST":
        acc = request.POST.get('accessories')
        request.session['accessories'] = acc
        return redirect('/select_services')
    return render(request, 'select_accessories_intermediate.html')

def select_accessories_premium(request):
    if request.method == "POST":
        acc = request.POST.get('accessories')
        request.session['accessories'] = acc
        return redirect('/select_services')
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

def kitchen_summary(request):
    context = {
    'layout' : request.session.get('layout'),
    'name' : request.session.get('name'),
    'loft1' : request.session.get('loft'),
    'package' : request.session.get('package'),
    'material' : request.session.get('material'),
    'countertop' : request.session.get('countertop'),
    'finish' : request.session.get('finsh'),
    'accessories' : request.session.get('accessories')
    }
    print(context)
    return render(request, 'kitchen_summary.html')

def kitchen_summary_buildpkg(request):
    return render(request, 'kitchen_summary_buildpkg.html')