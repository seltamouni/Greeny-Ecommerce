from .models import Comapny

def get_company_inf(request):
    company = Comapny.objects.last()
    return {'info':company}