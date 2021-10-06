from django.db import models
from django.contrib import admin

def download_csv(modeladmin, request, queryset):
    import csv
    f = open('some.csv', 'wb')
    writer = csv.writer(f)
    writer.writerow(["code", "country", "ip", "url", "count"])
    for s in queryset:
        writer.writerow([s.code, s.country, s.ip, s.url, s.count])


class StatAdmin(admin.ModelAdmin):
    list_display = ('code', 'country', 'ip', 'url', 'count')
    actions = [download_csv]
    
admin.site.register(Stat, StatAdmin)
