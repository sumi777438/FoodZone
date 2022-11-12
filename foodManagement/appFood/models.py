from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conatct(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    subject = models.CharField(max_length=250)
    message=models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Table"


class Team(models.Model):
    name=models.CharField(max_length=255)
    desinignation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team')
    added_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


CATEGORY_CHOICE=(
    ('Burger','Burger'),
    ('Pizza','Pizza'),
    ('Snacks','Snacks'),
    ('sweet','sweet'),

    )

class Dish(models.Model):
    name=models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='dishes/%Y/%m/%d')
    category=models.CharField(choices=CATEGORY_CHOICE,max_length=6,null=True)
    selling_price = models.FloatField(default=0)
    discount_price = models.FloatField()
    is_available =models.BooleanField(True)
    added_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='profile/%Y/%m/%d',null=True,blank=True)
    contact_number=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True)
    update_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
    class Meta:
        verbose_name_plural = "Profile Table"

class Order(models.Model):
    customer=models.ForeignKey(Profile,on_delete=models.CASCADE)
    item=models.ForeignKey(Dish,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    invoice_id=models.CharField(max_length=100,blank=True)
    payer_id=models.CharField(max_length=100,blank=True)
    order_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer.user.first_name



class Forget(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    creted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
