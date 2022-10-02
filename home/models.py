from django.db import models

# Create your models here.
class Contact(models.Model):
    reg_no = models.AutoField(primary_key=True)
    reg_number= models.CharField(max_length=30,default=1000)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=35)
    phone = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=500)
    tempaddress = models.CharField(max_length=500)
    edu = models.CharField(max_length=50)
    exp = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    # filename=models.FileField(upload_to='media', blank="true", null="true")
    filename= models.FileField(upload_to='files/', null=False, verbose_name="" )
    
    
    
    def __str__(self):
        return self.name
    
    
    def __str__(self):
        return self.name + ": " + str(self.filename)
