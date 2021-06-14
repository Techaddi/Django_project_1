from django.shortcuts import render,redirect
from .models import Dest, Message, Service,Contact,Orders
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.views.decorators.csrf import csrf_exempt

from .PayTm import Checksum


MERCHANT_KEY = 'your merchant key'

# Create your views here.
def index(request):
    dests=Dest.objects.all().order_by('-id')[:2]
    msgs=Message.objects.all()
    sers=Service.objects.all()
    context={
        'dests':dests,
        'msgs' :msgs,
        'sers' :sers

    }
    return render(request, 'index.html',context)
def about(request):
    
    return render(request, 'index.html')
def services(request):
    
    return render(request, 'index.html')
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        number=request.POST.get('number','')
        message=request.POST.get('message','')
        print(name, email, number, message)
        contact=Contact(name=name,email=email,number=number,message=message)
        contact.save()
        messages.info(request,'Detail send')
        return redirect('/')
    else:

        return render(request, 'index.html')
def form(request):
    return render(request, 'checkout.html')

def checkout(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone', '')
        order = Orders( name=name, email=email, address=address, 
                       state=state, phone=phone, amount=amount)
        order.save()
        #return render(request, 'checkout.html', {'thank':thank, 'id': id})
        param_dict = {

            'MID': 'merchant id',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

    
        return  render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'checkout.html')


@csrf_exempt 
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})