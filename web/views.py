from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'web/turshilt/base.html', {})

def help(request): 
    return render(request, 'web/turshilt/pages/help.html')

def about(request):
    return render(request, 'web/turshilt/pages/about.html')

def personal_line(request):
    return render(request, 'web/turshilt/pages/personal_line.html')

def leasing_line(request):
    return render(request, 'web/turshilt/pages/leasing_line.html')

def auto(request):
    return render(request, 'web/turshilt/pages/auto.html')

def student(request):
    return render(request, 'web/turshilt/pages/student.html')

def women(request):
    return render(request, 'web/turshilt/pages/women.html')

def farmer(request):
    return render(request, 'web/turshilt/pages/farmer.html')