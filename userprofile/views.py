## Models
from .models import UserProfile
from django.contrib.auth.models import User, Group
from core.models import Branch, Config

#functions

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

# upload files
from django.core.files.storage import default_storage
from PIL import Image

@login_required
def account(request):
    if 'buttonUpdateAccount' in request.POST:
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        phone_number = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        tin = request.POST.get('tin')
        sss = request.POST.get('sss')
        philhealth = request.POST.get('philhealth')
        pagibig = request.POST.get('pagibig')
        emergency_contact = request.POST.get('emergencyContact')
        emergency_contact_number=request.POST.get('emergencyContactNumber')
        birthdate = request.POST.get('birthdate')
        pk = request.user.id
        user = User.objects.get(id=pk)
        user.email = email
        user.save()
        userprofile = UserProfile.objects.update_or_create(
            user=user,
            defaults={
                'first_name':first_name,
                'last_name':last_name,
                'phone_number':phone_number,
                'address':address,
                'tin':tin,
                'sss':sss,
                'pagibig':pagibig,
                'philhealth':philhealth,
                'emergency_contact':emergency_contact,
                'emergency_contact_number':emergency_contact_number,
                'birthdate':birthdate,
            }
        )
        if request.FILES.get('upload'):
            upload = request.FILES['upload']
            uploaded_image = Image.open(upload) # No need to use StringIO
            thumbnail_image = uploaded_image.resize((100, 100)) # Create the thumbnail
            file_path = f'avatars/{upload.name}'
            default_storage.save(file_path, upload)
            userimage = UserProfile.objects.get(user=user)
            userimage.avatar = file_path
            userimage.save()
        messages.success(request,'Account updated')
    elif 'buttonDeactivate' in request.POST:
        return deactivate(request)
    return render(request,'userprofile_account.html')

@login_required
def account_config(request):
    user = request.user
    groups = Group.objects.all().order_by('name')
    u_group = user.groups.all()
    user_group = []
    for g in u_group:
        user_group.append(g.name)
    context = {
        'groups':groups,
        'user_group':user_group,}
    if 'submitButton' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(id=user.pk)
        user.set_password(password)
        user.username = username
        user.save()
        messages.success(request,'Account updated.')
        return redirect('userprofile:config')
    if 'updateRoleButton' in request.POST:
        for group in groups:
            group.user_set.remove(user)
            if str(group.pk) in request.POST:
                group.user_set.add(user)
                messages.success(request,f'{group.name} is assigned.')
            else:
                pass
        return redirect('userprofile:config')
    else:
        pass
    return render(request,'userprofile_account_config.html', context)

@login_required
def deactivate(request):
    if 'buttonDeactivate' in request.POST:
        verification = request.POST.get('accountActivation')
        if verification == 'on':
            user = request.user
            user.is_active = False
            user.save()
            messages.success(request, 'Account deactivated.')
            return redirect('core:login')
    else:
        messages.error(request,'Oops. Something went wrong.' )
        return redirect('core:account')


@login_required
@permission_required('core.can_view_users', raise_exception=True)
def users_view(request):
    context={}
    user = request.user
    company = user.userprofile.company
    branch = get_object_or_404(Branch, pk=pk)
    config = Config.objects.get(company=company)
    page_content_count = config.page_content_number
    if branch.company == company:
        users = UserProfile.objects.filter(branch=branch.pk)
        paginator=Paginator(users,page_content_count)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        page_range = paginator.page_range
        context['page'] = page
        context['page_range'] = page_range
        context['users'] = page
        context['branch'] = branch
        return render(request,'core-company-settings-branch-view-users.html', context)
    else:
        return redirect('core:branch')