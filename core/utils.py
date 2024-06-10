# Settings
from django.conf import settings
# models
from django.contrib.auth.models import User, Group
from userprofile.models import UserProfile
from .models import Company, Branch, Config, STOCK_DEDUCTION_CHOICES
# functions
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import render,redirect, HttpResponseRedirect , get_object_or_404
from django.urls import reverse

from .forms import RegistrationForm
# upload files
from django.core.files.storage import default_storage
from PIL import Image


class Validate():
    def __init__(self, request):
        self.user = request.user
        self.company = self.user.userprofile.company
        self.config = Config.objects.get(company=self.user.userprofile.company)

class EasyPage():
    def __init__(self,request, table, page_num):
        paginator = Paginator(table, Validate(request).config.page_content_number)
        self.objects = paginator.get_page(page_num)
        page_range = paginator.page_range
        self.context = {
            'page':self.objects,
            'page_range':page_range,
        }