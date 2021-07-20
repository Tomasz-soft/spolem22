from django.contrib import admin

# Register your models here.
from promocje.models import Promocje,PozProm
from towary.models import Towary


admin.site.register(Promocje)
admin.site.register(PozProm)
admin.site.register(Towary)
