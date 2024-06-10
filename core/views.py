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
from django.shortcuts import render,redirect, HttpResponseRedirect , get_object_or_404
from django.urls import reverse

from .forms import RegistrationForm
from .utils import Validate , EasyPage
# upload files
from django.core.files.storage import default_storage
from PIL import Image

@login_required
def home(request):
    return render(request, 'base.html')

def login_page(request):
    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            user = request.user
            profile = UserProfile.objects.get(user=user.id)
            if profile.company is None:
                print('tiggered')
                return redirect('core:company_register')
            else:
                messages.success(request,'Welcome to Pipalite!')
                return redirect('core:home')
        else:
            messages.error(request,'Username or password is incorrect.')
            return render(request,'core-login.html')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('core:home'))
        else:
            return render(request, 'core-login.html')

def registration(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST': 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user1 = User.objects.create_user(username=username, password=password)
            user1.is_active = False
            user1.save()
            messages.success(request,'Accounted is created for '+ username + '. Contact administrator for approval')
            return redirect('core:login')
        else:
            messages.error(request,'Something went wrong.')
            return redirect('core:registration')
    else:
        form = RegistrationForm()
        template = 'core-registration.html'
    context = {
        'form':form
    }
    return render(request, template, context)

def logout_view(request):
    logout(request)
    messages.success(request,'Logout successful')
    return redirect('core:login')

def handler404_view(request, exception):
    return render(request, 'core-404.html', status=404)

@login_required
def company_register(request):
    user = request.user
    profile = UserProfile.objects.get(user=user.pk)
    if profile.company is None:
        if request.method == 'POST':
            if 'getCompany' in request.POST:
                return render(request,'core-company-get-code.html')
            if 'addCompany' in request.POST:
                return render(request, 'core-company-get-code.html')
        else:
            return render(request,'core-register-company.html')
    else:
        return redirect('core:login')
    
def add_code(request):
    if 'getCodeButton' in request.POST:
        code = request.POST.get('companyCode')
        if Company.objects.filter(code=code).exists():
            try: 
                company = Company.objects.get(code=code)
            except:
                messages.error(request,'No matching code.')
            user=request.user
            branch = Branch.objects.filter(company=company)
            profile = UserProfile.objects.get(user=user)
            profile.branch = branch[0]
            profile.company = company
            profile.save()
            group_name=settings.DEFAULT_ROLE_ON_CODE_ADD
            group = Group.objects.get(name=group_name)
            group.user_set.add(user)
            messages.success(request,f'Welcome to {company.name}!')
            return redirect('core:home')
        else: 
            messages.error(request,'No matching code.')
            return render(request, 'core-company-get-code.html')
    return render(request,'core-company-get-code.html')

def add_company(request):
    if 'createCompanyButton' in request.POST:
        name = request.POST.get('companyName')
        tagline = request.POST.get('tagline')
        address = request.POST.get('address')
        tax_id = request.POST.get('tax_id')
        contact_number = request.POST.get('contactNumber')
        email = request.POST.get('email')
        stock_deduction_type = request.POST.get('stockDeductionType')
        if request.FILES.get('logo'):
            upload = request.FILES['logo']
            file_path = f'company/{upload.name}'
            default_storage.save(file_path, upload)
        else:
            filepath= settings.DEFAULT_COMPANY_LOGO
        company = Company.objects.create(
            name=name,
            logo=filepath,
            tagline=tagline,
            address=address,
            tax_id=tax_id,
            contact_num=contact_number,
            email=email, 
            stock_deduction_type=stock_deduction_type,
        )
        branch = Branch.objects.create(
            name=name,
            logo=filepath,
            tagline=tagline,
            address=address,
            tax_id=tax_id,
            contact_num=contact_number,
            email=email,
            company=company, 
        )
        config = Config.objects.create(
            company = company, 
            page_content_number = settings.DEFAULT_PAGE_NUMBER_ON_MAKE
        )
        user = request.user
        group_name=settings.DEFAULT_ROLE_ON_COMPANY_ADD
        group = Group.objects.get(name=group_name)
        group.user_set.add(user)
        profile = UserProfile.objects.get(user=user.pk)
        profile.company = company
        profile.branch = branch
        profile.save()
        return redirect('core:login')
    return render(request, 'core-company-add.html')

@login_required
@permission_required('core.can_update_settings', raise_exception=True)
def company_edit_view(request):
    if 'buttonEditCompany' in request.POST:
        user = request.user
        name = request.POST.get('companyName')
        tagline = request.POST.get('tagline')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact_num = request.POST.get('contactNumber')
        tax_id = request.POST.get('taxID')
        sdt = request.POST.get('stockDeductionType')
        company = user.userprofile.company
        company.name = name
        company.tagline = tagline
        company.email = email
        company.address=address
        company.contact_num = contact_num
        company.tax_id = tax_id
        company.stock_deduction_type = sdt
        if request.FILES.get('upload'):
            uploaded_logo = request.FILES['upload']
            file_path = f'company/{uploaded_logo.name}'
            default_storage.save(file_path, uploaded_logo)
            company.logo = file_path
        if request.FILES.get('headerInput'):
            uploaded_logo = request.FILES['headerInput']
            file_path_header = f'company/{uploaded_logo.name}'
            file_header = default_storage.save(file_path_header,uploaded_logo)
            company.header_logo = file_header
        messages.success(request,'Account updated')
        company.save()
    stock_deduction_type_choices = settings.STOCK_DEDUCTION_CHOICES
    context = {
        'stock_deduction_choices':stock_deduction_type_choices,
    }
    return render(request,'core-company-settings.html', context)

@login_required
@permission_required('core.can_update_settings', raise_exception=True)

def branch_list_view(request):
    user = request.user
    company = user.userprofile.company
    branches = Branch.objects.filter(company=company)
    context = {
        'branches':branches,
        'company':company,
    }
    return render(request,'core-company-settings-branch.html', context)

@login_required
@permission_required('core.can_update_settings', raise_exception=True)
def branch_edit_view(request,pk):
    user = request.user
    company = user.userprofile.company
    branch = get_object_or_404(Branch, pk=pk)
    if branch.company == company:
        context = {
            'branch':branch,
        }
        if 'buttonSubmit' in request.POST:
            name = request.POST.get('branchName')
            tagline = request.POST.get('tagline')
            email = request.POST.get('email')
            address = request.POST.get('address')
            contact_num = request.POST.get('contactNumber')
            tax_id = request.POST.get('taxID')
            branch.name = name
            branch.tagline = tagline
            branch.email = email
            branch.address=address
            branch.contact_num = contact_num
            branch.tax_id = tax_id
            if request.FILES.get('upload'):
                uploaded_logo = request.FILES['upload']
                file_path = f'company/{uploaded_logo.name}'
                default_storage.save(file_path, uploaded_logo)
                branch.logo = file_path
            if request.FILES.get('headerInput'):
                uploaded_logo = request.FILES['headerInput']
                file_path_header = f'company/{uploaded_logo.name}'
                file_header = default_storage.save(file_path_header,uploaded_logo)
                branch.header_logo = file_header
            branch.save()
            messages.success(request,'Account updated')
            return redirect('core:branch')
        else:
            return render(request,'core-company-settings-branch-edit.html', context)
    else:
        return redirect('core:branch')
    

@login_required
@permission_required('core.can_update_settings', raise_exception=True)
def branch_view_users(request, pk):
    validator = Validate(request)
    branch = get_object_or_404(Branch, pk=pk)
    if branch.company == validator.company:
        users = UserProfile.objects.filter(branch=branch.pk)
        page_num = request.GET.get('page')
        page = EasyPage(request,users,page_num)
        context = page.context
        context['users'] = page.objects
        context['branch'] = branch
        return render(request,'core-company-settings-branch-view-users.html', context)
    else:
        return redirect('core:branch')