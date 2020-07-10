from django.db import models


class Contact(models.Model):
    name=models.CharField(max_length=250,default='',unique=True)



    def __str__(self):
        return self.name


        
class Detaile(models.Model):
        name =models.ForeignKey(Contact,on_delete=models.CASCADE)
        phone = models.CharField(max_length=1000,default='')
        gmail=models.CharField(max_length=1000,default='')
        place=models.CharField(max_length=1000,default='')
