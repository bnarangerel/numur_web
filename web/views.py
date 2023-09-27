from django.shortcuts import render
from web.models import News
from web.models import Slide
from web.models import Loan_type
from web.models import Merchant
from web.models import Contract_location
from web.models import General_contract_loc
import json
# Create your views here.
def base(request):
    return render(request, 'web/turshilt/base.html', {})

def main(request):
    news = News.objects.all()
    slides = Slide.objects.all()
    loan_types = Loan_type.objects.all()
    
    return render(request, 'web/turshilt/pages/main.html', {
        'news': news,
        'slides': slides,
        'loan_types': loan_types
    })

def help(request): 
    return render(request, 'web/turshilt/pages/help.html')

def about(request):
    return render(request, 'web/turshilt/pages/about.html')

def personal_line(request):
    return render(request, 'web/turshilt/pages/personal_line.html')

def leasing_line(request):
    merchants = Merchant.objects.filter(is_active = True)
    return render(request, 'web/turshilt/pages/leasing_line.html', {
        'merchants': merchants
    })

def auto(request):
    return render(request, 'web/turshilt/pages/auto.html')

def student(request):
    return render(request, 'web/turshilt/pages/student.html')

def women(request):
    return render(request, 'web/turshilt/pages/women.html')

def farmer(request):
    news = News.objects.all()
    return render(request, 'web/turshilt/pages/farmer.html', {
        'news': news
    })

def contract(request):
    contract_locs_ub = Contract_location.objects.filter(contract_loc_type = 'Улаанбаатар')
    contract_locs_country = Contract_location.objects.filter(contract_loc_type = 'Орон нутаг')
    # general_types = General_contract_loc.objects.all()
    return render(request, 'web/turshilt/pages/contract.html',{
        'contract_locs_ub': contract_locs_ub,
        'contract_locs_country': contract_locs_country
        # 'general_types' : general_types
    })