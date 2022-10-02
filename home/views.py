from sequences import get_next_value
from django.shortcuts import render
from .models import Contact
from django.contrib import messages


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def career(request):
    if request.method == "POST":
        reg_number=get_next_value('reg_number')
        print(reg_number)
        name =request.POST.get('name')
        
        gender =request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
            
        address = request.POST.get('address')
        tempaddress = request.POST.get('tempaddress')
        edu = request.POST.get('edu')
        exp = request.POST.get('exp') 
        status = request.POST.get('status')
        filename= request.FILES.get('filename')
        
        
     
        # if name !="" or gender!="" or email !="" or phone != "" or address != "" or tempaddress!= ""  or edu != "" or exp != "" or status!= "" or filename !="":
            
        #     messages.warning(request, "please enter All the details")
        
        # elif len(name)<2  or len(email)<3  or len(phone)<10 or len(edu)<4 or filename=="":
        #     messages.error(request, "Please fill the form correctly")
        # else:
        contact = Contact(reg_number=reg_number,name=name,gender=gender, email=email,phone=phone,address=address,tempaddress=tempaddress,edu=edu,exp=exp,status=status,filename=filename)
        
        contact.save()
        
        messages.success(request, "Your Form has been submitted successfully.")
        # smtp server login here
            


#         send_mail(
#     'registration mail',
#     'Hi...'+ name +'   this is computer generated mail thank you for registering with we save your response and we will contact you your reg no is :'+'KPIV'+str(reg_number)+ 'please note this number',
#     'ashnew1226@gmail.com',
#     [email],
#     fail_silently=False,
# )
        
        html_content = render_to_string('email_template.html', {'name':name.upper(), 'reg_number':reg_number}) # render with dynamic value
        text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives("Registration Mail", text_content, 'kpinfotechvidyapeeth@gmail.com', [email,phone])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        

        # # Your Account SID from twilio.com/console
        # account_sid = "AC136b1f57bf5872f4ed1986b8c4c8968f"
        # # Your Auth Token from twilio.com/console
        # auth_token  = "48e7e052a3fdcd6589e5712d54a19f83"

        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #     to=phone, 
        #     from_="+19036183381",
        #     body="Hello from Python!")

        # print(message.sid)
    else:
        "plase fill all feilds"
        
    return render(request, 'home/career.html')
