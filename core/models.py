from django.db import models
import uuid

MA = 'MA'
FIFO = 'FIFO'
STOCK_DEDUCTION_CHOICES = ((MA,'MA'),(FIFO,'FIFO'))

class Company (models.Model):
    name = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='company', default='company/default.png')
    header_logo = models.ImageField(upload_to='company', default='defaults/default_header.png')
    tagline = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=250, null=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    contact_num = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    stock_deduction_type = models.CharField(max_length=4,choices=STOCK_DEDUCTION_CHOICES,default=MA)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name 
    
    class Meta:
        permissions = (('can_update_settings', 'Can update/modify company settings.'),)

class Branch (models.Model):
    name = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='company', default='company/default.png')
    header_logo = models.ImageField(upload_to='company', default='defaults/default_header.png')
    tagline = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=250, null=True)
    tax_id = models.CharField(max_length=100, null=True, blank=True)
    contact_num = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.name 

class Config(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, primary_key=True, blank=False, null=False)
    page_content_number = models.PositiveIntegerField(null=False, blank=False)