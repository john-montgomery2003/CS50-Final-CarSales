from django.contrib import admin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SliderNumericFilter
from django.contrib.admin import ModelAdmin, SimpleListFilter
from .models import car
from .models import Message
from rangefilter.filter import DateRangeFilter


class carAdmin(NumericFilterModelAdmin,admin.ModelAdmin):
	list_display = ('model','make', 'year', 'cost', 'milage', 'postDate','new', 'sold')
	search_fields = ('make', 'model')
	list_filter = (('year', SliderNumericFilter),('cost', SliderNumericFilter), ('milage', SliderNumericFilter),'new', 'sold', ('postDate', DateRangeFilter))

class messageAdmin(admin.ModelAdmin):
	search_fields = ('email','text')
	list_filter = ('responded',)
# Register your models here.

admin.site.register(car, carAdmin)
admin.site.register(Message, messageAdmin)
