from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail as sm
from django.conf import settings as conf_settings

from .models import News
import socket


def home(request):
    if request.method == 'POST':
        time = request.POST['home_time']
        scheldule = request.POST['home_scheldule']
        address = request.POST['home_address']
        name = request.POST['home_name']
        phone = request.POST['home_phone']
        email = request.POST['home_email']
        message = request.POST['home_message']
        home_text_all = 'Tên : '+name+'<br>Thời gian : '+time+'<br>Lịch : '+scheldule+'<br>Địa chỉ : '+address+'<br>Phone : '+phone+'<br>email : '+email+'<br>Nội dung : '+message
        # socket.getaddrinfo('gmail.com', 80)
        # #send email to default address
        # send_mail(
        #     'Follow up required for - ' + name,
        #     message,
        #     email,
        #     [conf_settings.CONTACT_US_FORM_EMAIL_TO],
        #     fail_silently=False,
        # )
        res = sm(
                subject = '[Khách hàng]Booking',
                message = home_text_all,
                from_email = email,
                recipient_list = ['huynguyen@saigonbooks.vn'],
                fail_silently=False,
            )    
        messages.success(request, f'Hi {name}, Thanks for contacting us. We will follow up with you within next few business days.')
        return redirect('/')
    else:
        news = News.objects.all()[0:3]
        context = {'news': news}
        print(vars(news[0]))
        return render(request, 'website/home.html',context)

def about(request):
    return render(request, 'website/about.html')
        
def service(request):
    return render(request, 'website/service.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def blog(request):
    return render(request, 'website/blog.html')

def blog_details(request, pk):
    return render(request, 'website/blog_details.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['message_name']
        email = request.POST['message_email']
        message = request.POST['message']
        # socket.getaddrinfo('gmail.com', 80)
        # #send email to default address
        # send_mail(
        #     'Follow up required for - ' + name,
        #     message,
        #     email,
        #     [conf_settings.CONTACT_US_FORM_EMAIL_TO],
        #     fail_silently=False,
        # )
        res = sm(
                subject = '[Khách hàng]Liên hệ',
                message = message,
                from_email = email,
                recipient_list = ['huynguyen@saigonbooks.vn'],
                fail_silently=False,
            )    
        messages.success(request, f'Hi {name}, Thanks for contacting us. We will follow up with you within next few business days.')
        return redirect('contact')
    else:
        return render(request, 'website/contact.html')


