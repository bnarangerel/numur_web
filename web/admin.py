from django.contrib import admin
from .models import News
from .models import Slide
from .models import Loan_type
from .models import Merchant
from .models import General_contract_loc
from .models import Contract_location

admin.site.register(Loan_type)
admin.site.register(News)
admin.site.register(Slide)
admin.site.register(Merchant)
admin.site.register(General_contract_loc)
admin.site.register(Contract_location)