from django.db import models

# Create your models here.


class Addingemployee(models.Model):
    admin = models.CharField(max_length = 25)
    employeeid = models.CharField(max_length = 25)    
    employeename = models.CharField(max_length = 25)    
    employeeemail = models.EmailField()    
    employeephonenumber = models.CharField(max_length = 25)    
    employeerole = models.CharField(max_length = 25)    
    employeesalary = models.CharField(max_length = 25)    
    employeeaddress = models.TextField()    

    def __str__(self):
        return self.admin
       
    
class Contactus(models.Model):
    name = models.CharField(max_length = 25)
    email = models.EmailField()
    subject = models.CharField(max_length = 25)
    description = models.TextField()

    def __str__(self):
        return self.email    