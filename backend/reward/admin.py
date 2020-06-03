from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Rem

from django.db import models
from django.forms import Textarea


#
# @admin.register(Rem)
# class RemAdmin(ImportExportModelAdmin):
#     pass



admin.site.register(Rem)

