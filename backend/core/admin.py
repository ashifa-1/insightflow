from django.contrib import admin

# Register your models here.
from .models import (
    Workspace,
    WorkspaceMembership,
    Event
)


admin.site.register(Workspace)
admin.site.register(WorkspaceMembership)
admin.site.register(Event)