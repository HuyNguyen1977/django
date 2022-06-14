from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail as sm
from django.conf import settings as conf_settings

from .models import News, Topic
# from .models import Blogs
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
        # news = News.objects.get(topic_id='1')[0:3]
        news = News.objects.select_related('topic').filter(topic__code__icontains='news')
        # news = News.objects.raw('SELECT * FROM website_news')[0:3]
        blog = News.objects.get(slug='bang-gia-dieu-tri')
        context = {'news': news, 'blogs': blog}
        
        # print(vars(blog))
        # print(vars(news[0]))
        return render(request, 'website/home.html',context)

def qa(request):
    news = News.objects.select_related('topic').filter(topic__code__icontains='chtg')
    print(vars(news[0]))
    context = {'news': news}
    return render(request, 'website/qa.html', context)
        
def service(request):
    return render(request, 'website/service.html')

def pricing(request):
    blog = News.objects.get(slug='bang-gia-dieu-tri')
    context = {'blogs': blog}
    return render(request, 'website/pricing.html', context)

def blog(request):
    # news = News.objects.all()[0:5]
    # # blog = News.objects.get(slug='bang-gia-dieu-tri')
    # context = {'news': news}
    # return render(request, 'website/blog.html', context)
    Allblog = News.objects.all().order_by('-id') [0:5]
    blog = Allblog[0]
    context = {'Allblogs': Allblog, 'blogs': blog}
    return render(request, 'website/blog_details.html', context)

# def blog_details(request):
    
#     Allblog = News.objects.all().order_by('-id') [0:5]
#     blog = Allblog[0]
#     context = {'Allblogs': Allblog, 'blogs': blog}
    
#     return render(request, 'website/blog_details.html', context)

def blog_details(request, pk ):
    
    Allblog = News.objects.all() [0:5]
    blog = News.objects.get(slug=pk)
    print(vars(blog))
    context = {'blogs': blog, 'Allblogs': Allblog}
    
    return render(request, 'website/blog_details.html', context)



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


