from django.db import models
from django.conf import settings
from django.utils import timezone
        
def make_img_path(pathfolder):
    img_path = f"images/{pathfolder}/"
    return img_path 

# Create your models here.
class News(models.Model):
        
    def make_img_path(pathfolder):
        img_path = f"images/{pathfolder}/"
        return img_path 
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=200, default='Нөмөр')
    title = models.CharField(max_length=200)
    text = models.TextField()
    img_caption = models.CharField(max_length=50, blank=True, null=True)
    img_url = models.ImageField(upload_to=make_img_path("news/%y"), default= 'path_to_default_image.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    url = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Slide(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    loan_name = models.CharField(max_length=200)
    loan_interest = models.CharField(max_length=200, blank=True, null=True)
    loan_text = models.TextField()
    img_caption = models.CharField(max_length=50, blank=True, null=True)
    img_url = models.ImageField(upload_to=make_img_path("slide/%y"), default= 'path_to_default_image.jpg')
    created_date = models.DateTimeField(default=timezone.now)
    url = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.loan_name

class Loan_type(models.Model):
    loan_name = models.CharField(max_length=200)
    loan_description = models.TextField()
    loan_page_url = models.CharField(max_length=200, default="http://127.0.0.1:8000/")
    icon_caption = models.CharField(max_length=50, blank=True, null=True, default="numur")
    icon = models.ImageField(upload_to=make_img_path("icons/%y"), default= 'path_to_default_image.png')
    
    def __str__(self):
        return self.loan_name
    
class Merchant(models.Model):
    merchant_name = models.CharField(max_length=200)
    merchant_phone_number = models.CharField(max_length=9)
    fb_url = models.CharField(max_length=200, default="")
    merchant_logo = models.ImageField(upload_to=make_img_path("merchant/%y"), default= 'path_to_default_image.jpg')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.merchant_name
    
    def format_phone_number(self):
        number = self.merchant_phone_number
        digits_only = ''.join(filter(str.isdigit, number))
        if len(digits_only) >= 8:
            return digits_only[:4] + '-' + digits_only[4:8]
        else:
            return number
        
class General_contract_loc(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.name
    
class Contract_location(models.Model):
    name = models.CharField(max_length=200)
    contract_loc_type = models.ForeignKey(General_contract_loc, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number1 = models.CharField(max_length=8, null=True, blank=True, default=None)
    phone_number2 = models.CharField(max_length=8, null=True, blank=True, default=None)
    description = models.TextField(null=True, blank=True, default=None, )
    time_table = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
        

    

    