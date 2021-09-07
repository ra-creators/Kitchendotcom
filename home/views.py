from django.http.response import HttpResponse
from django.http import HttpResponseRedirect  
from django.shortcuts import redirect, render  
from home .models import c_details, kitchen_details, Constants # importing calculation model is removed
# FOR STORING LIST IN DATABASE FIELDS NAMELY APPLIANCES AND SERVICES

rate = {
'hdhmr' : 1200,
'mrply' : 1000,
'bwrply' : 1200,
'bwpply' : 1500,
'laminate' : 400,
'pvclaminate' : 700 ,
'asacrylic' : 1000, 
'glossypu' : 1200, 
'basic' : 300,
'intermediate' : 500,
'premium' : 1000}

# Create your views here.
def kitchen_price_steps(request):
    # request.session['name'] = 'test'
    return render(request, 'kitchen_price_steps.html')

def select_layout(request):
    if request.method == "POST":
        layout = request.POST.get('kitchenLayout')
        request.session['layout'] = layout 
        return redirect('/customer_details')
      
    return render(request, 'select_layout.html')

def customer_details(request):
    layout = request.session.get('layout')
    # store the choise and details of customer here
    # context = kitchen_details.objects.all().last()
    # selected_layout = sizeof(context)
    # print(type(selected_layout))
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        request.session['name'] = name
        request.session['email'] = email
        request.session['phone'] = phone

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
        return redirect('/select_loft_type')
    return render(request, 'select_ushape.html')


def select_loft_type(request):
    
    if request.method == "POST":
        loft1 = request.POST.get('loft_type') # this keyword depends on template
        if loft1 == "custom":
            loft1 = request.POST.get('loft')
            # request.session['loft'] = loft1 # for if condition
        request.session['loft'] = loft1     # for else condition
        return redirect('/select_package')
    return render(request, "select_loft_type.html")

def select_package(request):  # fqname is not confirmed
    
    # to be entered in following 4 function
    if request.method == "POST":    
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
    
        if package == "ownpackage":
            return redirect('/build_package')
        if package == "essentials":
            request.session['material'] = "MR Plywood"
            request.session['finish'] = "Laminate"
            request.session['accessories'] = "Wire Basket"
            return redirect('/summary')
        if package == "premium":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "PVC"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')
        if package == "luxe":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "Acrylic"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')

    return render(request, 'select_package.html') # 1.template name is not confirmed

def select_package_essentials(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
       
        if package == "ownpackage":
            return redirect('/build_package')
        if package == "essentials":
            request.session['material'] = "MR Plywood"
            request.session['finish'] = "Laminate"
            request.session['accessories'] = "Wire Basket"
            return redirect('/summary')
        if package == "premium":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "PVC"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')
        if package == "luxe":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "Acrylic"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')
    
    return render(request, 'select_package_essentials.html')

def select_package_luxe(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        
        if package == "ownpackage":
            return redirect('/build_package')
        if package == "essentials":
            request.session['material'] = "MR Plywood"
            request.session['finish'] = "Laminate"
            request.session['accessories'] = "Wire Basket"
            return redirect('/summary')
        if package == "premium":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "PVC"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')
        if package == "luxe":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "Acrylic"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')
        
    return render(request, 'select_package_luxe.html')

def select_package_premium(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        
        if package == "ownpackage":
            return redirect('/build_package')
        if package == "essentials":
            request.session['material'] = "MR Plywood"
            request.session['finish'] = "Laminate"
            request.session['accessories'] = "Wire Basket"
            return redirect('/summary')
        if package == "premium":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "PVC"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')
        if package == "luxe":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "Acrylic"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')

    return render(request, 'select_package_premium.html')

def select_package_buildpkg(request):
    if request.method == "POST":
        package = request.POST.get('package') # "package" <- this name might be different
        request.session['package'] = package
        
        if package == "ownpackage":
            return redirect('/build_package')
        if package == "essentials":
            request.session['material'] = "MR Plywood"
            request.session['finish'] = "Laminate"
            request.session['accessories'] = "Wire Basket"
            return redirect('/summary')
        if package == "premium":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "PVC"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')
        if package == "luxe":
            request.session['material'] = "HDHMR"
            request.session['finish'] = "Acrylic"
            request.session['accessories'] = "Tandem Basket"
            return redirect('/summary')


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
        return redirect('/select_finish')
    return render(request, 'select_countertop.html')

def select_finish(request):
    if request.method == "POST":
        f = request.POST.get('finish')
        request.session['finish'] = f
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
        services_list = request.POST.getlist('service[]')
        request.session['services'] = services_list
        return redirect('/select_appliances')
    return render(request, 'select_services.html')


def select_appliances(request):
    if request.method == "POST":
        app_list = request.POST.getlist('appliance[]')
        print(app_list)
        request.session['appliances'] = app_list
        return redirect('/summary/buildpkg')
    return render(request, 'select_appliances.html')

def kitchen_summary(request):
    constant = Constants.objects.all().last()
    # key names are as per summary page
    context = {
        'name' : request.session.get('name'),
        'shape' : request.session.get('layout'),  
        'a_feet' : request.session.get('a_feet'),
        'a_inch' : request.session.get('a_inch'),
        'b_feet' : request.session.get('b_feet'),
        'b_inch' : request.session.get('b_inch'),
        'c_feet' : request.session.get('c_feet'),
        'c_inch' : request.session.get('c_inch'),
        'loft' : request.session.get('loft'),
        'type' : request.session.get('package'),
        'material' : request.session.get('material'),
        'finish' : request.session.get('finish'),
        'accessories' : request.session.get('accessories')
    }
    # Calculation part begins

    a = round(int(context['a_feet']) + (int(context['a_inch']) / 12), 2)
    b = round(int(context['b_feet']) + (int(context['b_inch']) / 12), 2)
    c = round(int(context['c_feet']) + (int(context['c_inch']) / 12), 2)
    l = int(context['loft'])

    if context['type'] == "essentials":
        cal = round((a+b+c) * (3+l) * int(constant.essentials), 2) # last value should be fetched from model
    elif context['type'] == "premium":
        cal = round((a+b+c) * (3+l) * int(constant.premium), 2) # last value should be fetched from model
    elif context['type'] == "luxe":
        cal = round((a+b+c) * (3+l) * int(constant.luxe), 2) # last value should be fetched from model
    print(a,b,c,l, cal)
    # Calculation part ends
    size = str(round(a,2)) + "ft x " + str(round(b,2)) + "ft x " + str(round(c,2)) + "ft"
    details = kitchen_details(Shape = context['shape'], Size = size, Loft = context['loft'], Type = context['type'], Accessories = context['accessories'], Material = context['material'], Finish = context['finish'],Price = cal)
    details.save()
    context['size'] = size
    context['price'] = cal
    return render(request, 'kitchen_summary.html', {'context': context}) 

def kitchen_summary_buildpkg(request):
    constant = Constants.objects.all().last()
    # key names are as per summary page
    context = {
    'shape' : request.session.get('layout'),  
    'name' : request.session.get('name'),
    'a_feet' : request.session.get('a_feet'),
    'a_inch' : request.session.get('a_inch'),
    'b_feet' : request.session.get('b_feet'),
    'b_inch' : request.session.get('b_inch'),
    'c_feet' : request.session.get('c_feet'),
    'c_inch' : request.session.get('c_inch'),
    'name' : request.session.get('name'),
    'loft' : request.session.get('loft'),
    'type' : request.session.get('package'),
    'material' : request.session.get('material'),
    'countertop' : request.session.get('countertop'),
    'finish' : request.session.get('finish'),
    'accessories' : request.session.get('accessories'),
    'services' :  request.session.get('services'),
    'appliances' :  request.session.get('appliances')
    }
  
    # Calculation part begins
    a = round(int(context['a_feet']) + (int(context['a_inch']) / 12), 2)
    b = round(int(context['b_feet']) + (int(context['b_inch']) / 12), 2)
    c = round(int(context['c_feet']) + (int(context['c_inch']) / 12), 2)
    l = int(context['loft'])
    
    size = str(round(a,2)) + "ft x " + str(round(b,2)) + "ft x " + str(round(c,2)) + "ft"
    # calculation of pricing
    if context['countertop'] == "Yes":
         cal = round(((a+b+c) * (3+l) * (rate[context['material']] + rate[context['finish']] + rate[context['accessories']])+ int(constant.countertop)), 2)
    else:
        cal = round(((a+b+c) * (3+l) * (rate[context['material']]+rate[context['finish']]+ rate[context['accessories']])), 2)
    # Calculation part end
    print(a,b,c,l, cal)
    details = kitchen_details(Name = context['name'], Shape = context['shape'], Size = size, Type = context['type'], Material = context['material'], Countertop = context['countertop'], Loft = context['loft'], Finish = context['finish'], Accessories = context['accessories'], Appliances = context['appliances'], Services = context['services'], Price = cal)
    details.save()
    context['size'] = size
    context['price'] = cal
    return render(request, 'kitchen_summary_buildpkg.html', {'context': context})
