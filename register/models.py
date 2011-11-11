from django.db import models
import datetime

# Create your models here.

class User(models.Model):
   user_name = models.CharField(max_length=200)
   password = models.CharField(max_length=200)
   verification_flag = models.CharField(max_length=20)
   

class PersonalDetails(models.Model):
   first_name = models.CharField(max_length=200)
   last_name = models.CharField(max_length=200)
   gender  =  models.CharField(max_length=1)
   education  =  models.CharField(max_length=20)
   father_name = models.CharField(max_length=200)
   mother_name = models.CharField(max_length=200)
   current_address  =  models.CharField(max_length=200)
   city = models.CharField(max_length=200)
   pincode = models.CharField(max_length=6)
   permanent_address  =  models.CharField(max_length=200)
   telephone =  models.CharField(max_length=13)
   mobile =   models.CharField(max_length=13)
   user = models.OneToOneField(User)
 
class EmploymentDetails(models.Model):
   company_type = models.CharField(max_length=200)
   designation = models.CharField(max_length=200)
   income  =  models.FloatField()
   work_years  =  models.IntegerField(max_length=2)
   name = models.CharField(max_length=200)
   office_address  =  models.CharField(max_length=200)
   city = models.CharField(max_length=200)
   pincode = models.CharField(max_length=6)
   email_id =   models.CharField(max_length=50) 
   user = models.OneToOneField(User)

class BankDetails(models.Model):
   account_number = models.CharField(max_length=20)
   bankname = models.CharField(max_length=200)
   branch_address  =  models.CharField(max_length=200)
   account_type =   models.CharField(max_length=20)
   user = models.OneToOneField(User)
   
   
class Statement(models.Model):
   transaction_date = models.DateTimeField('date of transaction')
   amount = models.FloatField()
   to_account  =  models.CharField(max_length=20)
   transacion_id =   models.CharField(max_length=20)    
   
   
class Card(models.Model):
   card_number = models.CharField(max_length=200)
   card_type = models.CharField(max_length=200)	
   interest = models.FloatField()
   credited_amount = models.FloatField()
   user = models.OneToOneField(User)
   
   

   
	#....
   #def __unicode__(self):
	#  return self.question
   #def was_published_today(self):
    #  return self.pub_date.date() == datetime.date.today()	

