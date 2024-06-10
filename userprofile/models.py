from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from django_resized import ResizedImageField
from inventory.models import Warehouse
from core.models import Company, Branch
import os

class UserProfile(models.Model):
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    avatar = ResizedImageField(size=[300, 300],upload_to='avatars', default='avatars/default.png', blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True,blank=True)
    last_name = models.CharField(max_length=30, null=True,blank=True)
    tin = models.CharField(max_length=30, null=True,blank=True)
    sss = models.CharField(max_length=30, null=True,blank=True)
    pagibig = models.CharField(max_length=30, null=True,blank=True)
    philhealth = models.CharField(max_length=30, null=True,blank=True)
    emergency_contact = models.CharField(max_length=50, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=20, null=True, blank=True)
    birthdate = models.DateField(auto_now_add=True, blank=True)
    #foreignkeys
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        permissions = (('can_modify_role', 'Can modify own role.'),
                       ('can_view_users', 'Can view other users.'),
                       ('can_modify_users','Can modify other users'))

    def __str__(self):
        return f'{self.user.username} Profile' 

def create_profile(sender, instance, created, **kwargs):
    if created: 
        profile=UserProfile(user=instance)
        profile.save()

post_save.connect(create_profile, sender=User)