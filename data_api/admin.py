from django.contrib import admin
from .models import User
from .models import Checklist_item
from .models import Room,Issue_report,checkoff_list

admin.site.register(User)
admin.site.register(Checklist_item)
admin.site.register(Room)
admin.site.register(Issue_report)
#admin.site.register(list_items)
admin.site.register(checkoff_list)

# Register your models here.
