from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images",null=True)
    description=models.CharField(max_length=300)
    product_details=models.CharField(max_length=400)
    price=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.product_name



class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="images",null=True)
    address=models.CharField(max_length=300)
    place=models.CharField(max_length=200)
    contact_number=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)


class Questions(models.Model):
    description=models.CharField(max_length=200)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="questions")
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
    class Meta:
        ordering=["-created_date"]

    @property
    def question_answer(self):
        return Questions.objects.filter(questions=self)

class Answers(models.Model):
    questions=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="answers")
    created_date=models.DateTimeField(auto_now_add=True)

class carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(("product added ","product added"),
             ("product removed","product removed"),
    )
    status=models.CharField(max_length=200,choices=options,default="product added")
    qty=models.PositiveIntegerField(default=1)


class Soldoutproducts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="soldout")
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    options=(
        ("soldout","soldout"),
    )
    status=models.CharField(max_length=200,choices=options,default="soldout")
